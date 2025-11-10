import json
import os
import pandas as pd
from typing import Dict, List, Union

def load_config() -> Dict:
    """Load configuration from JSON file."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "data", "testdata.json")
    with open(config_path) as file:
        return json.load(file)

def load_csv(file_name: str = "Book1.csv") -> Dict[str, str]:
    # Get the absolute path to the data directory
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    file_path = os.path.join(data_dir, file_name)
    """
    Load data from a CSV file with one column and no headers.
    Returns a dictionary with the expected keys for login testing.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found at: {file_path}")
    try:
        # Read CSV file without headers
        df = pd.read_csv(file_path, header=None)
        
        # Return a dictionary with the expected keys
        return {
            "url": df.iloc[0, 0].strip() if len(df) > 0 else "",
            "username": df.iloc[1, 0].strip() if len(df) > 1 else "",
            "password": df.iloc[2, 0].strip() if len(df) > 2 else ""
        }
    except pd.errors.EmptyDataError:
        return {"url": "", "username": "", "password": ""}
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")
