# Data

**Target dataset (real-data upgrade):** [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
— ~1,067,371 real transactions from a UK online retailer (2009–2011).

## How to obtain
1. Download `online_retail_II.xlsx` from the UCI link above (or the Kaggle mirror).
2. Place it in this `data/` folder.
3. Run the notebook — it will clean the data (remove cancellations/returns, negative quantities, missing customer IDs), engineer RFM features per customer, and build a forward-looking 6-month spend target.

The raw file is kept out of git via `.gitignore`.

> The currently committed notebook uses a synthetic RFM generator; the real-data version replaces it as described in the repo README roadmap.
