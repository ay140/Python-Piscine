import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame, prints its dimensions,
    and returns it. Handles exceptions by returning None.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame or None: The dataset if successful, or None
        if an exception occurs or the path is invalid.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception:
        return None
