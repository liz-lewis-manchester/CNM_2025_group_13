import numpy as np
import pandas as pd
def interpolate_initial_conditions(sensor_data: pd.DataFrame, x_grid: np.ndarray) -> np.ndarray:
    """Interpolates sensor data onto the model's spatial grid."""
    x_sensor = sensor_data['x']
    theta_sensor = sensor_data['concentration']
    theta_interpolated = np.interp(x_grid, x_sensor, theta_sensor)
    return theta_interpolated
