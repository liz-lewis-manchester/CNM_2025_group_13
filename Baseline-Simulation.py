#Initialise conditions
L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 0.1
C[0] = 250.0
C_history = np.zeros((N_t, N_x))

#Importing functions
import numpy as np

import os
!rm -rf CNM_2025_group13
!git clong https://github.com/liz-lewis-manchester/CNM_2025_group_13.git
if not os.path.exists('/content/CNM_2025_group_13'):
  !git clone https://github.com/liz-lewis-manchester/CNM_2025_group_13.git

import sys
sys.path.append('/content/CNM_2025_group_13')

from src.solver import storing_matrix, forward_substitution
from src.domain import setup_domain, initial_conditions
from src.boundary import apply_outflow_boundary

#Initialise domain
x_array, t_array, N_x, N_t, Delta_x, Delta_t, = setup_domain(L, T, Delta_x, Delta_t)
C_current, C_next = initial_conditions(N_x, C, initial_index, N_t)

#Running functions to set up grid
x_array, t_array, N_x, N_t = setup_domain(L, T, Delta_x, Delta_t)
C_current, C_next = initial_conditions(N_x, C0, start_index=0)

#Running function to compute coefficients A and B
A, B = storing_matrix(N_x, Delta_t, Delta_x, U)

#Creating a placeholder to store all the C values computed in the forward substitution
C_history = np.zeros((N_t, N_x))
C_history[0, :] = C_current

#Writing a loop to run the code and solve using forward substitution
for n in range (1, N_t):
  F = (1 / Delta_t) * C_current[1:]
  C_next[:] = 0.0
  C_next[0] = C0
  C_next = forward_substitution(A, B, F, C_next)
  C_current[:] = C_next[:]
  C_current = C_next.copy()
  C_history[n, :] = C_current
  apply_outflow_boundary(C_next)

#save results
RESULTS_FOLDER = "Results"
import os
os.makedirs(RESULTS_FOLDER, exist_ok=True)

#Plot concentration vs x
import matplotlib.pyplot as plt
time_plots = [0, N_t // 4, N_t // 2, N_t * 3 // 4, N_t - 1]
plot_times = t_array[time_plots]

plt.figure(figsize=(10, 6))
plt.title("Baseline Simulation at Fixed Velocity (CFL={U * Delta_t / Delta_x: .1f})")
plt.xlabel("Distance along river (M)")
plt.ylabel("Pollutant cpncentration (µg/m^3)")

for i, n in enumerate(time_plots):
  plt.plot(x_array, C_history[n, :])

#saving graph
import os
RESULTS_FOLDER = "Results"
os.makedirs(RESULTS_FOLDER, exist_ok=True)
plt.savefig(
  os.path.join(RESULTS_FOLDER, "task7_baseline_simulation.png"),
  dpi=300
  bbox_inches="tight"
)
plt.show()

Print('Every line represents a different time')



