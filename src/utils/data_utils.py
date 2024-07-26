# utils/data_utils.py
import pandas as pd
import numpy as np

def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def save_csv(data, file_path):
    """Save a pandas DataFrame to a CSV file."""
    data.to_csv(file_path, index=False)

def split_data(data, test_size=0.2, random_state=42):
    """Split a pandas DataFrame into training and testing sets."""
    from sklearn.model_selection import train_test_split
    return train_test_split(data, test_size=test_size, random_state=random_state)

def convert_to_numpy(data):
    """Convert a pandas DataFrame to a NumPy array."""
    return data.values
