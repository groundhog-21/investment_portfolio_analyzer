INVESTMENT PORTFOLIO ANALYZER
=============================

Purpose
-------
A Python-based tool for analyzing the performance of investment portfolios
against a blended benchmark index composed of equities, fixed income,
and liquidity components.

Daily Python Challenge - Day 1
------------------------------
This project was initiated as part of a Daily Python Challenge series.
Day 1 focused on:
 - Selecting representative tickers from yfinance to construct a portfolio benchmark 
 - Building a 10+ year dataset of adjusted prices for the benchmark
 - Establishing target weights for the benchmark components
 - Saving benchmark data and metadata in reusable formats (Parquet, CSV, JSON)

Folder Structure
----------------
investment_portfolio_analyzer/
│
├── notebooks/
│   └── 01_build_benchmark.ipynb     ← Day 1 notebook (interactive)
│
├── portfolio_analyzer/
│   ├── __init__.py
│   └── build_benchmark.py           ← Core benchmark-building logic
│
├── data/                            ← Local data only (excluded from Git)
│   ├── benchmark_tickers.json            ← User-defined benchmark tickers by asset class
│   ├── benchmark_weights.json            ← Calculated benchmark weights (sum = 1.0)
│   ├── benchmark_metadata.json           ← ETF metadata (fund name, category, inception date, etc.)
│   ├── benchmark_prices_named.csv        ← Benchmark prices (daily adjusted close)
│   ├── benchmark_prices_named.parquet    ← Same data in compact Parquet format
│   └── .gitkeep                          ← Placeholder to retain folder structure
│
├── requirements.txt
├── .gitignore
├── .gitattributes
├── LICENSE
└── README.txt


Getting Started
---------------
1. Create a virtual environment:
       python -m venv .venv
       .venv\Scripts\activate   (Windows)
2. Install dependencies:
       pip install -r requirements.txt
3. Run the Day 1 notebook in /notebooks.

License
-------
MIT License – see LICENSE file for details.