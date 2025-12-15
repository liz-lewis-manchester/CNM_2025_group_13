import numpy as np 
import matplotlib.pyplot as plt
from src.code import read_initial_conditions 
from src.interp import interpolate_initial_conditions
from src.solver import forward_substitution
from src.boundary import apply_inflow_boundary, apply_outflow_boundary
from src.coefficients import compute_coefficients
from src.velocity import constant_velocity
from src.plotting import plot_snapshot, plot_evolution

#Domain Parameters 
T = 5.0 * 60.0 #Total simulation time converted from minutes to seconds 
L = 20.0 #Length 
Delta_x = 0.2 
Delta_t = 10.0
U = 0.1 #River flow velocity 
C0 = 250.0 #Pollutant concentration at the inlet 

N_x = int(L / Delta_x) + 1
N_t = int(T / Delta_t) +1 
x_array = np.linspace(0, L, N_x) #Creating an array for x-coordinates 
t_array = np.linspace(0, T, N_t) #Creating an array for time points 

csv_data = read_initial_conditions('initial_conditions.csv')
C_current = interpolate_initial_conditions(csv_data, x_array)
C_next = C_current.copy()

C_history = np.zeros((N_t, N_x))
C_history[0, :] = C_current[:]

for n in range(1, N_t): #Loop
   u = constant_velocity(U, N_x) #Velocity Field
   A, B = compute_coefficients(u, Delta_t, Delta_x)

   C_new = forward_substitution(A, B, C_current, left_bc=C0) #Solving the Linear system

#Applying boundary conditions 
   current_time = n * Delta_t
   apply_inflow_boundary(C_new, current_time, U)
   apply_outflow_boundary(C_new)

#Updates and saves to history 
   C_current = C_new.copy()
   C_history[n, :] = C_current[:]

#Plotting results 
time_indices = [0, int(0.2 * N_t), int(0.5 * N_t), N_t-1]
plot_times = [t_array[n] for n in time_indices]


plt.figure(figsize=(10, 6)) #Created the plot 
for i, n in enumerate(time_indices):
  plt.plot(x_array, C_history[n,:], label = f't = {plot_times[i]/60:.1f}min')

plt.xlabel("distance along river (m)")
plt.ylabel("Pollutant concentration (μg/m³)")
plt.title("Task 8: Simulation with CSV Initial Conditions")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/task8_csv_simulation.png") 
plt.show()

print(f"Task 8 complete: CSV-based simulation saved to results/task8_csv_simulation.png")
