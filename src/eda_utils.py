import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Set up logging for error handling robustness
logging.basicConfig(level=logging.INFO)

def load_insurance_data(file_path):
    """Loads insurance data safely with exception handling."""
    try:
        df = pd.read_csv(file_path)
        logging.info("Data loaded successfully with " + str(df.shape) + " rows.")
        return df
    except FileNotFoundError:
        logging.error("Error: The data file at " + file_path + " was not found.")
        return None
    except Exception as e:
        logging.error("An unexpected error occurred: " + str(e))
        return None

def calculate_loss_ratio(df, group_by_col=None):
    """Calculates the business loss ratio globally or grouped by a specific column."""
    if group_by_col:
        grouped = df.groupby(group_by_col)
        return grouped['TotalClaims'].sum() / grouped['TotalPremium'].sum()
    return df['TotalClaims'].sum() / df['TotalPremium'].sum()