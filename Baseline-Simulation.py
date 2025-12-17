#Initialise conditions
L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 0.1
C[0] = 250.0
C_history = np.zeros((N_t, N_x))

#Initialise domain
x_array, t_array, N_x, N_t, Delta_x, Delta_t, = setup_domain(L, T, Delta_x, Delta_t)
C_current, C_next = initial_conditions(N_x, C, initial_index, N_t)

#run solver
for n in range (1, N_t):
  C_next = forward_substitution(C_current, Delta_x, Delta_t, U)
  C_current = C_next.copy()
  C_history[n, :] = C_current[:]
  #add conditions from task 4
  def apply_inflow_boundary(C_next: np.ndarray, current_time: float, U: float) -> None:
     SOURCE_CONCENTRATION = 250.0 # µg/m³
    if current_time >= 0:
        C_next[0] = SOURCE_CONCENTRATION
  def apply_outflow_boundary(C_next: np.ndarray) -> None:
    last_index = len(C_next) - 1
    C_next[last_index] = C_next[last_index - 1]
  for t_step in range(Nt):
    apply_inflow_boundary(C_next, current_time, U) 
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



