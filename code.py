import numpy as np
import pandas as pd

def interpolate_initial_conditions(sensor_data: pd.DataFrame, x_grid: np.ndarray) -> np.ndarray:
    """
    Interpolates sensor data onto the model's spatial grid.
    Args:
        sensor_data: DataFrame with 'x' (distance) and 'concentration' columns.
        x_grid: The 1D numpy array representing the model's grid points.
    Returns:
        np.ndarray: The pollutant concentration at each point in x_grid.
    """
    # Extract sensor data
    x_sensor = sensor_data['x'].to_numpy() 
    theta_sensor = sensor_data['concentration'].to_numpy() 
    sort_indices = np.argsort(x_sensor)
    x_sensor_sorted = x_sensor[sort_indices]
    theta_sensor_sorted = theta_sensor[sort_indices]
    theta_interpolated = np.interp(
        x_grid, 
        x_sensor_sorted, 
        theta_sensor_sorted
    )

    return theta_interpolated
