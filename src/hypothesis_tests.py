import pandas as pd
from scipy import stats
import logging

logging.basicConfig(level=logging.INFO)

def test_numerical_groups(df, group_col, target_col, group1, group2):
    """
    Performs a Two-Sample T-Test to check if the means of a numerical column 
    are statistically different between two distinct groups.
    """
    try:
        # Filter the data for the two specific groups
        data1 = df[df[group_col] == group1][target_col].dropna()
        data2 = df[df[group_col] == group2][target_col].dropna()
        
        # Calculate means for business reference
        mean1, mean2 = data1.mean(), data2.mean()
        
        # Run the T-test
        t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False)
        
        return {
            "group1_mean": mean1,
            "group2_mean": mean2,
            "t_statistic": t_stat,
            "p_value": p_value,
            "significant": p_value < 0.05
        }
    except Exception as e:
        logging.error("Error executing numerical group hypothesis test: " + str(e))
        return None