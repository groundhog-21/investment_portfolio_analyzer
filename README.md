# Investment Portfolio Analyzer

A simplified, lightweight Python project designed to analyze an investment
portfolio relative to a custom benchmark using real historical price data.

This project is structured around clear daily steps:

---

## 📅 Day 1 — Build the Benchmark

The Day 1 notebook (`01_build_benchmark.ipynb`) does the following:

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

The benchmark data will be used in later steps for portfolio comparison.

---

## Repository Structure

investment_portfolio_analyzer/
├── data/ # All saved data files
├── notebooks/ # Jupyter notebooks for each development step
│ └── 01_build_benchmark.ipynb
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── .gitattributes

---

## Installation

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

---

## Install dependencies:
pip install -r requirements.txt

---

## Requirements

Python 3.12+
Jupyter or VS Code with the Jupyter extension
Internet access (for yfinance price downloads)

---

## Future Work

Day 2: Build the portfolio data with the same unified structure.
Day 3: Compare portfolio vs. benchmark performance.

---