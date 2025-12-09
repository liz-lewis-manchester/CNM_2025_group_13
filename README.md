def read_initial_conditions(filepath: str) -> pd.DataFrame:
    """Reads initial pollutant concentrations from a CSV file."""
    import pandas as pd
    data = pd.read_csv(initial_conditions.csv)
    return data
