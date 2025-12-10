# CNM_2025_group_13
#Setup parameters
L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 0.1
C = 250.0

#setup domain
x_array, t_array, N_x, N_t, Delta_x, Delta_t, = intialise_grid(L, T, Delta_x, Delta_t)
C_current, C_next = apply_initial_condition(N_X, C, initial_index)

#store results
C_history = np.zeros((N_t, N_x))
C_history[0, :] = C_current[:]

#run forward subsitution solver 
for n in range (1, N_t):
  #code for solver 

#save results to results/folder
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

np.save(os.path.join(results_folder, 'x_grid.npy'), x_array)
np.save(os.path.join(results_folder, 't_steps.npy'), t_array)
np.save(os.path.join(results_folder, 'C_history_baseline.npy'), C_history)
print(f"💾 Saved {C_history.shape} solution history to '{results_folder}/'")

#plot concentration vs x at selected times
time_indices = [0, int(0.2 * Nt), int(0.5 * Nt), Nt - 1] # Select t=0, 20%, 50%, and final time
plot_times = [t_array[n] for n in time_indices]
plt.figure(figsize=(10, 6))
plt.title("Baseline simulation (fixed velocity)")
plt.xlabel("Distance along river (M)")
plt.ylabel("Pollutant concentration (µg/m^3)")

for i, n in enumerate(time_indices):      #iterates the times to plot
  plt.plot(x_array, C_history[n, :])      #plots graph

plt.legend()
