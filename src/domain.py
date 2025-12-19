import numpy as np
import pandas as pd


#Task 1:setting up the doamin
def setup_domain(L, T, Delta_x, Delta_t):
  N_x = int(L / Delta_x) + 1
  N_t = int(T / Delta_t) + 1
  x_array = np.linspace(0, L, N_x)
  t_array = np.linspace(0, T, N_t)

  return x_array, t_array, N_x, N_t

def initial_conditions(N_x, C0, start_index=0):
  C_current = np.zeros(N_x)
  C_next = C_current.copy()
  C_current[start_index]=C0

  return C_current, C_next
  

#Task 5:Reading initial conditions from file 
def read_initial_conditions(filepath: str) -> pd.DataFrame:
    """Reads initial pollutant concentrations from a CSV file."""
    import pandas as pd
    data = pd.read_csv(filepath)
    return data


#Task 6: Interpolating the data from file into the grid 
def interpolate_initial_conditions(sensor_data: pd.DataFrame, x_grid: np.ndarray) -> np.ndarray:
    """
    Interpolates sensor data onto the model's spatial grid.
    Args:
        sensor_data: DataFrame with 'Distance (m)' (distance) and 'Concentration (µg/m_ )' columns.
        x_grid: The 1D numpy array representing the model's grid points.
    Returns:
        np.ndarray: The pollutant concentration at each point in x_grid.
    """
    # Extract sensor data
    x_sensor = sensor_data['Distance (m)'].to_numpy() 
    theta_sensor = sensor_data['Concentration (µg/m_ )'].to_numpy() 
    sort_indices = np.argsort(x_sensor)
    x_sensor_sorted = x_sensor[sort_indices]
    theta_sensor_sorted = theta_sensor[sort_indices]
    theta_interpolated = np.interp(
        x_grid, 
        x_sensor_sorted, 
        theta_sensor_sorted
    )

    return theta_interpolated
