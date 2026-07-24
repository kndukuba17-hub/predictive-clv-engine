# 💷 Predictive Customer Lifetime Value (CLV) Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-EC4E20)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-8A2BE2)
![Status](https://img.shields.io/badge/Status-Real--data%20upgrade%20in%20progress-yellow)

Predicting how much a retail customer will spend over the next 6 months from **RFM (Recency, Frequency, Monetary) behaviour**, and using SHAP to explain *which behaviours drive value* — so CRM teams can spot future VIPs early and target retention spend.

> **Behavioural angle:** CLV is fundamentally a behavioural prediction — it asks how a customer's past *actions* (how recently, how often, how much they buy) predict their future ones. SHAP turns that into a ranked, explainable driver list a marketing team can act on.

---

## ⚠️ Data status (honest note)
The committed notebook currently trains on a **synthetic RFM dataset** generated in-notebook. That's fine for demonstrating the modelling pipeline, but it can't show real data-cleaning challenges — so this repo is being upgraded to the real **[UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)** dataset (~1M real transactions), from which genuine RFM features and a forward-looking spend target are engineered. This README will be updated with measured metrics once the real-data version lands.

## ⚙️ Approach
1. **RFM feature engineering** — Recency (days since last order), Frequency (order count), Monetary (average basket value), plus engagement signals (email open rate, returns).
2. **Modelling** — an **XGBoost Regressor** predicts the continuous 6-month spend value (regression, not a yes/no classification).
3. **Explainability** — **SHAP** `TreeExplainer` ranks the behavioural drivers of value, so the output is an actionable strategy, not a black box.
4. **Evaluation** — MAE and R² on a held-out test set.

## 🧰 Tech Stack
Python · pandas · NumPy · scikit-learn (`StandardScaler`, `train_test_split`) · XGBoost · SHAP · Matplotlib · Seaborn

---

## 📁 Repository Structure
```
├── README.md
├── requirements.txt
├── notebooks/
│   └── predictive_clv_engine.ipynb
├── src/
├── data/          # UCI Online Retail II download instructions — see data/README.md
├── images/
└── docs/
```

## 🚀 How to Run
```bash
git clone https://github.com/kndukuba17-hub/predictive-clv-engine.git
cd predictive-clv-engine
pip install -r requirements.txt
jupyter notebook notebooks/predictive_clv_engine.ipynb
```
Runs on Jupyter or Google Colab.

## 🗺️ Roadmap
- Swap synthetic RFM data for real **UCI Online Retail II** transactions and re-report metrics.
- Add a customer VIP-segmentation view (quantile bands on predicted CLV).
- Compare XGBoost against a simpler linear baseline to justify the model choice.
