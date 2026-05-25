# Insurance-risk-analytics
## Data Version Control (DVC)

This project uses DVC to track datasets.

### Reproduce data:

1. Clone repo:
   git clone <repo-url>

2. Install DVC:
   pip install dvc

3. Pull data:
   dvc pull

This will download all datasets from local storage.
# Insurance Risk Analytics

An end-to-end data engineering and predictive analytics project analyzing historical car insurance policies to uncover geographic risk trends, monitor portfolio profitability, and predict future claims.

## Project Architecture
* `data/`: Local repository data managed and versioned via DVC.
* `notebooks/`: Contains exploratory data analysis, hypothesis testing, and model iteration.
* `src/`: Modular, reusable production python scripts with error logging.

## Core Insights from Task 1
* **Portfolio Health:** Global portfolio Loss Ratio stands at 52.8%.
* **Regional Disparities:** Risk exposure peaks in the Somali region (61.2% Loss Ratio) and drops to its lowest in Amhara (47.8%).
* **Data Quality:** The dataset contains 10,000 entries with 0 missing values across all features.