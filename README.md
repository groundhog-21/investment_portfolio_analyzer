📘 Investment Portfolio Analyzer

A lightweight, reproducible Python workflow for constructing a benchmark, modeling an investment portfolio, and comparing their historical performance over a consistent rolling 15-year window.

📅 Day 1 — Build the Benchmark

Notebook: 01_build_benchmark.ipynb

Day 1 constructs the primary benchmark used throughout the project.

This notebook:

Defines benchmark tickers and weights

Downloads 15 years of daily Close prices ending today

Retrieves fund names for verification

Computes the benchmark price series

Saves benchmark artifacts to the /data directory

Saved files:

benchmark_tickers.json

benchmark_weights.json

benchmark_names.json

benchmark_prices.csv

benchmark_prices.parquet

📅 Day 2 — Construct the Portfolio

Notebook: 02_build_portfolio.ipynb

Day 2 defines the investment portfolio to be compared with the benchmark.

This notebook:

Defines portfolio tickers and asset classes

Defines user-input weights and computes normalized weights

Downloads the same 15-year Close price window

Retrieves fund names for verification

Saves portfolio artifacts to /data

Saved files:

portfolio_tickers.json

normalized_portfolio_weights.json

portfolio_names.json

portfolio_prices.csv

portfolio_prices.parquet

📅 Day 3 — Compare Portfolio vs Benchmark

Notebook: 03_compare_portfolio_vs_benchmark.ipynb

This notebook:

Loads benchmark & portfolio price data

Aligns daily return history over the common 15-year window

Computes:

Cumulative returns

Calendar-year returns

Full-period annualized returns

Annualized volatility

Sharpe ratio (RF = 0)

Produces comparison charts

No new files are saved in Day 3.

📅 Day 4 — Additional Benchmarks

Notebook: 04_additional_benchmarks.ipynb

Day 4 extends the analysis by introducing three additional benchmark allocation strategies:

U.S. benchmark (VTI + BND)

Ex-U.S. developed benchmark (VEA + IGOV)

U.S. aggressive benchmark (VTI + BND)

This notebook:

Downloads 15-year Close price history for benchmark ETFs

Computes weighted daily returns

Compares cumulative, annualized, and calendar-year performance

Produces benchmark comparison charts

No Day 4 artifacts are saved to /data.

📁 Repository Structure
investment_portfolio_analyzer/
│
├── data/
│   └── .gitkeep
│
├── notebooks/
│   ├── 01_build_benchmark.ipynb
│   ├── 02_build_portfolio.ipynb
│   ├── 03_compare_portfolio_vs_benchmark.ipynb
│   └── 04_additional_benchmarks.ipynb
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── .gitattributes

⚙️ Installation

Create a virtual environment (optional but recommended):

python -m venv venv


Activate it:

macOS / Linux

source venv/bin/activate


Windows

venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

📦 Requirements
pandas
numpy
matplotlib
yfinance
pyarrow
python-dateutil