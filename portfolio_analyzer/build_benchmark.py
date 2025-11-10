"""
build_benchmark.py
------------------
Core functions for constructing the benchmark dataset.

This module handles:
- collecting metadata for benchmark components
- fetching price data from yfinance
- saving data in reusable formats

Used on Day 1 of the Investment Portfolio Analyzer project.
"""

# ---------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------
import yfinance as yf
import pandas as pd
import json
import os


# ---------------------------------------------------------------------
# 🧩 Metadata Collection
# ---------------------------------------------------------------------
def get_ticker_metadata(ticker):
    """
    Retrieve metadata for a single ticker from yfinance.

    Returns:
        dict with ticker information
    """
    t = yf.Ticker(ticker)
    info = t.info
    return {
        "ticker": ticker,
        "name": info.get("longName") or info.get("shortName"),
        "fund_family": info.get("fundFamily"),
        "provider": info.get("issuer") or info.get("fundFamily"),
        "category": info.get("category"),
        "inception_date": info.get("fundInceptionDate"),  # Unix timestamp
    }


def collect_metadata(benchmark_tickers):
    """
    Collect metadata for all tickers in the benchmark dictionary.

    Args:
        benchmark_tickers (dict): {segment: [tickers]}
    Returns:
        pd.DataFrame
    """
    metadata = []
    for segment, tickers in benchmark_tickers.items():
        for ticker in tickers:
            data = get_ticker_metadata(ticker)
            data["segment"] = segment
            metadata.append(data)

    metadata_df = pd.DataFrame(metadata)

    # Convert Unix timestamp → readable date
    metadata_df["inception_date"] = pd.to_datetime(
        metadata_df["inception_date"], unit="s", errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    return metadata_df


def save_metadata(metadata_df, output_dir="../data"):
    """Save metadata to JSON and CSV."""
    os.makedirs(output_dir, exist_ok=True)
    metadata_path = os.path.join(output_dir, "benchmark_metadata.json")
    metadata_df.to_json(metadata_path, orient="records", indent=4)
    print(f"✅ Metadata saved to {metadata_path}")


# ---------------------------------------------------------------------
# 🧩 Benchmark Data Fetching
# ---------------------------------------------------------------------
def get_benchmark_data_with_names(benchmark_tickers, start="2015-11-08", end="2025-11-07"):
    """
    Download daily adjusted prices for all benchmark tickers and
    label columns with fund names.

    Returns:
        pd.DataFrame: benchmark prices with readable names
    """
    tickers = [t for sublist in benchmark_tickers.values() for t in sublist]

    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    # Extract adjusted close (already adjusted)
    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Close"]
    else:
        prices = data[["Close"]]
        prices.columns = tickers

    # Retrieve fund names
    ticker_to_name = {}
    for t in tickers:
        try:
            info = yf.Ticker(t).info
            ticker_to_name[t] = info.get("longName") or info.get("shortName") or t
        except Exception as e:
            print(f"⚠️ Could not retrieve name for {t}: {e}")
            ticker_to_name[t] = t

    # Rename columns
    prices = prices.rename(columns=ticker_to_name).dropna(how="all").sort_index()

    print(f"✅ Benchmark data: {prices.shape[0]} days × {prices.shape[1]} tickers")
    print(f"   From {prices.index.min().date()} to {prices.index.max().date()}")
    return prices


def save_benchmark_data(prices, output_dir="../data"):
    """Save benchmark prices to CSV and Parquet formats."""
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "benchmark_prices_named.csv")
    parquet_path = os.path.join(output_dir, "benchmark_prices_named.parquet")

    prices.to_csv(csv_path)
    prices.to_parquet(parquet_path)

    print(f"✅ Saved CSV and Parquet data to {output_dir}")