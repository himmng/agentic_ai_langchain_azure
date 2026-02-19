import pandas as pd

def load_wa_data(filepath: str):
    return pd.read_csv(filepath)
