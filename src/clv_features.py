"""Reusable CLV data-prep and feature engineering for UCI Online Retail II.

Extracted from the notebook so the logic is importable and testable.

Example
-------
>>> import pandas as pd
>>> from clv_features import clean_transactions, build_customer_features
>>> raw = pd.read_excel("data/online_retail_II.xlsx", sheet_name=None)
>>> df = clean_transactions(pd.concat(raw.values(), ignore_index=True))
>>> features = build_customer_features(df, target_months=6)
"""
from __future__ import annotations
import pandas as pd

FEATURE_COLUMNS = [
    "recency_days", "tenure_days", "frequency", "monetary_total", "total_quantity",
    "distinct_products", "avg_unit_price", "avg_basket_value", "avg_items_per_order",
    "purchase_rate", "is_uk",
]


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Drop missing customers, cancellations and returns; add a Revenue column."""
    df = df.dropna(subset=["Customer ID"]).copy()
    df["Invoice"] = df["Invoice"].astype(str)
    df = df[~df["Invoice"].str.startswith("C")]                 # cancellations
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]           # returns / bad rows
    df["Customer ID"] = df["Customer ID"].astype(int)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Revenue"] = df["Quantity"] * df["Price"]
    return df


def build_customer_features(df: pd.DataFrame, target_months: int = 6) -> pd.DataFrame:
    """Time-split the data and engineer per-customer RFM features + a future-spend target.

    Features come only from the observation window (<= cutoff); the target is total
    spend in the `target_months` after the cutoff (0 for customers who do not return).
    """
    max_date = df["InvoiceDate"].max().normalize()
    cutoff = max_date - pd.DateOffset(months=target_months)
    obs = df[df["InvoiceDate"] <= cutoff]
    future = df[df["InvoiceDate"] > cutoff]

    g = obs.groupby("Customer ID")
    feat = pd.DataFrame({
        "recency_days":      (cutoff - g["InvoiceDate"].max()).dt.days,
        "tenure_days":       (cutoff - g["InvoiceDate"].min()).dt.days,
        "frequency":         g["Invoice"].nunique(),
        "monetary_total":    g["Revenue"].sum(),
        "total_quantity":    g["Quantity"].sum(),
        "distinct_products": g["StockCode"].nunique(),
        "avg_unit_price":    g["Price"].mean(),
    })
    feat["avg_basket_value"] = feat["monetary_total"] / feat["frequency"]
    feat["avg_items_per_order"] = feat["total_quantity"] / feat["frequency"]
    feat["purchase_rate"] = feat["frequency"] / (feat["tenure_days"] + 1)
    feat["is_uk"] = (
        obs.groupby("Customer ID")["Country"].agg(lambda s: s.mode().iloc[0])
        == "United Kingdom"
    ).astype(int)

    future_spend = future.groupby("Customer ID")["Revenue"].sum()
    feat["target_6m_spend"] = feat.index.map(future_spend).fillna(0.0)
    return feat
