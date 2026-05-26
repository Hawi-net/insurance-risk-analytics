import pandas as pd
import numpy as np
from scipy import stats
import logging

logging.basicConfig(level=logging.INFO)

def run_numerical_ttest(df, group_col, target_col, group_a, group_b):
    """
    Performs an Independent Two-Sample T-Test for numerical KPIs (Severity, Margin).
    """
    try:
        data_a = df[df[group_col] == group_a][target_col].dropna()
        data_b = df[df[group_col] == group_b][target_col].dropna()
        
        mean_a, mean_b = data_a.mean(), data_b.mean()
        t_stat, p_val = stats.ttest_ind(data_a, data_b, equal_var=False)
        
        return {
            "test_type": "Welch T-Test",
            "group_A_mean": mean_a,
            "group_B_mean": mean_b,
            "p_value": p_val,
            "reject_null": p_val < 0.05
        }
    except Exception as e:
        logging.error(f"Error running T-Test: {e}")
        return None

def run_categorical_chisquare(df, group_col, claim_flag_col, group_a, group_b):
    """
    Performs a Chi-Squared Test of Independence for categorical KPIs (Claim Frequency).
    """
    try:
        filtered_df = df[df[group_col].isin([group_a, group_b])]
        contingency_table = pd.crosstab(filtered_df[group_col], filtered_df[claim_flag_col])
        
        chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)
        
        freq_a = df[df[group_col] == group_a][claim_flag_col].mean()
        freq_b = df[df[group_col] == group_b][claim_flag_col].mean()
        
        return {
            "test_type": "Chi-Square",
            "group_A_freq": freq_a,
            "group_B_freq": freq_b,
            "p_value": p_val,
            "reject_null": p_val < 0.05
        }
    except Exception as e:
        logging.error(f"Error running Chi-Square: {e}")
        return None