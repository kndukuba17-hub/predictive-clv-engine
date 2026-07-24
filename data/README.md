# Data

**Dataset:** [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
— 1,067,371 real transactions from a UK online retailer (Dec 2009 – Dec 2011).

## One-step download
```bash
curl -L -o data/online_retail_II.zip "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"
unzip data/online_retail_II.zip -d data/
```
This produces `data/online_retail_II.xlsx` (~45 MB, two sheets). The notebook loads both
sheets, caches a `.pkl` for fast re-runs, and does all cleaning/feature engineering itself.

Raw data (`*.xlsx`, `*.zip`, `*.pkl`, `*.csv`) is kept out of git via `.gitignore`.
