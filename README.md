
# Insurance Risk Analytics

An end-to-end data engineering and predictive analytics project analyzing historical car insurance policies to uncover geographic risk trends, monitor portfolio profitability, and predict future claims.

---

## 🏗️ Project Architecture

```text
├── data/       # Local repository datasets managed and versioned via DVC.
├── notebooks/  # Contains exploratory data analysis, hypothesis testing, and model iteration.
├── reports/    # Generated visual evidence artifacts and performance plots.
└── src/        # Modular, reusable production Python scripts with error logging.


📈 Core Insights from Data Exploration (Task 1)Portfolio Health: Global portfolio Loss Ratio stands at 52.8%, indicating a stable baseline profitability profile.Regional Disparities: Risk exposure peaks significantly in the Somali region (61.2% Loss Ratio) and drops to its lowest in Amhara (47.8%).Data Quality: The dataset contains 10,000 clean entries with 0 missing values across all features, providing a highly reliable tracking foundation.⚙️ Engineering & Environment ControlsEnvironment Isolation: Fully decoupled dependencies running inside a dedicated .venv virtual environment targeting production-stable runtimes.Version Control Tree: Git tracking integrated natively for code review pipelines across distinct problem-solving branches (task-1 through task-4).Reproducible Pipeline: Modular utilities structured inside the src/ directory to seamlessly handle path routing, missing value assertions, and structured exception handling.🤖 Statistical Modeling & Risk Drivers (Task 4)To forecast financial liability, the project frames claim severity optimization by filtering historical data down exclusively to policies with active claims. We evaluated a baseline Linear Regression framework against an advanced Random Forest Ensemble to capture non-linear underwriting interactions.1. Performance Evaluation MatrixModeling ArchitectureRoot Mean Squared Error (RMSE)R² ScoreLinear Regression[Insert your LR RMSE here][Insert your LR R2 here]Random Forest Regressor[Insert your RF RMSE here][Insert your RF R2 here]

2. Strategic Risk Drivers
Using Mean Decrease in Impurity (MDI), the project extracted and plotted the top 5 strategic insurance risk features:

Asset Value: Evaluated as a primary driver of claim severity. Higher vehicle replacement values scale predicted financial liability substantially.

Geographic Profile: Regional features rank heavily in risk contribution, validating EDA findings that territorial underwriting variables must be dynamically priced into premium baselines.



