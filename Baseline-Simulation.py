#Initialise conditions
L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 0.1
C = 250.0

#Initialise domain
x_array, t_array, N_x, N_t, Delta_x, Delta_t, = setup_domain(L, T, Delta_x, Delta_t)
C_current, C_next = initial_conditions(N_x, C, initial_index, N_t)

#run solver
for n in range (1, N_t):
  C_next = advection_solver_step(C_current, Delta_x, Delta_t, U)
  C_current = C_next.copy()
  C_history[n, :] = C_current[:]

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



