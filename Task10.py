#Importing necessare functions 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#Importing codes fromm the repository
from src.domain import setup_domain
from src.solver import storing_matrix, forward_substitution
from src.boundary import apply_inflow_boundary, apply_outflow_boundary

# Creating a exponential decay function
def decaying_source_concentration(C0, t, decay_rate=0.01):
  return C0 * np.exp(-decay_rate * t)

# Interpolate initial conditions from CSV
def interpolate_initial_conditions(sensor_data, x_grid):
  x_sensor = sensor_data['Distance (m)'].to_numpy()
  C_sensor = sensor_data['Concentration (µg/m_ )'].to_numpy()
  idx = np.argsort(x_sensor)
  x_sorted = x_sensor[idx]
  C_sorted = C_sensor[idx]
  
  return np.interp(x_grid, x_sorted, C_sorted)

# MRunning the simulation
def run_simulation(U, Delta_x, Delta_t, L=20.0, T=300.0, C0=250.0, decay_rate=0.01):

  # Creating domain
  x_array, t_array, N_x, N_t = setup_domain(L, T, Delta_x, Delta_t)

  # Reading the file
  sensor_data = pd.read_csv("initial_conditions.csv", encoding="latin1")
  C_current = interpolate_initial_conditions(sensor_data, x_array)
  C_next = np.zeros_like(C_current)

  # Storing arrays
  C_history = np.zeros((N_t, N_x))
  C_history[0, :] = C_current[:]

  #Placeholder to store the valus of C
  source_history = np.zeros(N_t)
  source_history[0] = C0

  # Creating a time loop
  for n in range(1,N_t):
    current_time = n * Delta_t
    A,B = toring_matrix(N_x, Delta_t, Delta_x, U)

    # Compute source
    C_source = decaying_source_concentration(C0, current_time, decay_rate)

    F=(1/Delta_t)*C_current[1:]
    C_next= forward_substitution(A, B, F, C_next)

    # Applying boundaries
    C_next[0] = C_source
    apply_outflow_boundary(C_next)

    # Storing results
    C_current = C_new.copy()
    C_history[n,:] = C_current[:]
    source_history[n] = C_source
  return x_array,t_array,C_history,source_history 

#Setting up parameters
L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 0.1
C0 = 250.0
decay_rate = 0.01

# Constant source
x_const,t_const,C_const,source_const = run_simulation_with_source(U, Delta_x, Delta_t, L, T, C0,decay_rate=0.0)

# Decaying source
x_decay,t_decay,C_decay,source_decay = run_simulation_with_source(U, Delta_x, Delta_t, L, T, C0,decay_rate=decay_rate)

#Plotting the graphs
plt.plot(t_const/60, source_const, label="Constant source")
plt.plot(t_decay/60, source_decay, label=f"Decaying source (λ={decay_rate})") 
plt.xlabel("Time (minutes)") #creating lables
plt.ylabel("Source concentration (µg/m³)")
plt.title("Source Concentration vs Time") #creating title
plt.grid()
plt.legend()
plt.show() #Printing the graph


time_indices = [0, int(0.2*len(t_decay)), int(0.5*len(t_decay)), len(t_decay)-1] #creating time indice for the graph

plt.figure(figsize=(12, 7))
for n in time_indices:
  time_min = t_decay[n] / 60
  plt.plot(x_const, C_const[n], "--", label=f"t={time_min:.1f} min (constant)")
  plt.plot(x_decay, C_decay[n], "-", label=f"t={time_min:.1f} min (decaying)")

#Plotting the graph
plt.xlabel("Distance (m)")
plt.ylabel("Concentration (µg/m³)")
plt.title("Constant vs Decaying Source")
plt.grid()
plt.legend()
plt.show()

#Plotting graph showing differences 
plt.figure(figsize=(10, 6))
for n in time_indices:
  diff = C_const[n] - C_decay[n]
  plt.plot(x_decay, diff, label=f"t={t_decay[n]/60:.1f} min")

plt.xlabel("Distance (m)")
plt.ylabel("Difference (µg/m³)")
plt.title("Difference: Constant - Decaying Source")
plt.grid()
plt.legend()
plt.show()
