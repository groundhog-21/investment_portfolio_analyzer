# Investment Portfolio Analyzer

A simplified, lightweight Python project designed to analyze an investment portfolio relative to a custom benchmark using real historical price data.

This project is structured around clear, incremental daily steps.

---

## 📅 Day 1 — Build the Benchmark

The Day 1 notebook (`01_build_benchmark.ipynb`) performs the following:

- Defines a benchmark using a small set of tickers.
- Assigns simple benchmark weights.
- Fetches 10 years of daily historical price data using `yfinance`.
- Fetches fund names (sanity check only).
- Saves results into the `/data` folder:
  - `benchmark_tickers.json`
  - `benchmark_weights.json`
  - `benchmark_names.json`
  - `benchmark_prices.csv`
  - `benchmark_prices.parquet`

This benchmark dataset will be used in later steps for portfolio comparison.

---

## 📅 Day 2 — Build the Portfolio

The Day 2 notebook (`02_build_portfolio.ipynb`) performs the following:

- Defines the portfolio tickers (the actual holdings to be analyzed).
- Assigns portfolio weights (normalized so they sum to 1).
- Fetches 10 years of daily historical price data using `yfinance`.
- Fetches fund names (sanity check only).
- Saves results into the `/data` folder:
  - `portfolio_tickers.json`
  - `portfolio_weights.json` (normalized weights)
  - `portfolio_names.json`
  - `portfolio_prices.csv`
  - `portfolio_prices.parquet`

---

## 📅 Day 3 — Compare Portfolio vs Benchmark

The Day 3 notebook (`03_compare_portfolio_vs_benchmark.ipynb`) performs the following:

1. Loads benchmark and portfolio price data.
2. Computes **cumulative returns** over the entire data period.
3. Computes **calendar-year annualized returns**.
4. Computes **full-period annualized return**.
5. Calculates basic **risk/return metrics** (volatility, Sharpe ratio).
6. Visualizes cumulative return comparison.
7. Visualizes calendar-year return comparison.
8. Visualizes full-period annualized return comparison.

Day 3 provides the first full performance comparison between the benchmark and portfolio datasets produced in Days 1 and 2.

---

## Repository Structure

```text
investment_portfolio_analyzer/
├── data/                     # All saved data files (ignored by git)
│   ├── benchmark_tickers.json
│   ├── benchmark_weights.json
│   ├── benchmark_names.json
│   ├── benchmark_prices.csv
│   ├── benchmark_prices.parquet
│   ├── portfolio_tickers.json
│   ├── portfolio_weights.json
│   ├── portfolio_names.json
│   ├── portfolio_prices.csv
│   └── portfolio_prices.parquet
├── notebooks/
│   ├── 01_build_benchmark.ipynb
│   ├── 02_build_portfolio.ipynb
│   └── 03_compare_portfolio_vs_benchmark.ipynb
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── .gitattributes
```

> Note: The `data/` folder is ignored by git. Files are generated locally when you run the notebooks.

---

## Installation

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

- Python 3.12+
- Jupyter or VS Code with the Jupyter extension
- Internet access (for `yfinance` price downloads)

---

## Future Work

- Additional analysis (drawdowns, risk decomposition, rolling performance)
- Optional modularization into lightweight `.py` utilities

---

## License

This project is distributed under the MIT License. See `LICENSE` for details.