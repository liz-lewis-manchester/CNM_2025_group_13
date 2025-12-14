import numpy as np 
import matplotlib.pyplot as plt
from src.code import read_initial_conditions
from src.interp import interpolate_intitial_conditions 
from src.solver import forward_substitution
from src.boundary import apply_outflow_boundary
from src.coefficients import compute_coefficients 
from src.velocity import constant_velocity 

def decaying_source_concentration(C0,t,decay_rate=0.01):
  """
  Calculate exponentially decaying source concentration 
  C_source(t) = C0 * exp(-λt)

  Args:
      C0: Initial source concentration (μg/m³)
      t: Current time (seconds)
      decay_rate: Decay constant λ (1/seconds)

  Returns:
      Source concentration at time t
  """
  return C0 * np.exp(-decay_rate * t)

def apply_decaying_inflow_boundary(theta_new, current_time,C0,decay_rate):
  """
  Apply Dirichlet boundary condition at x=0 with decaying source
  """
  C_source = decaying_source_concentration(C0,current_time,decay_rate)
  theta_new[0] = C_source 

def run_simulation_with_source(decay_rate,L=20.0,T=300.0,Delta_x=0.2,Delta_t=10.0,U=0.1,C0=250.0):
  """
  Run simulation with specified decay rate
  decay_rate = 0 gives constant source (baseline)
  decay_rate > 0 gives exponentially decaying source 
  """
  N_x = int(L/Delta_x) + 1
  N_t = int(T/Delta_t) + 1
  x_array = np.linspace(0,L,N_x)
  t_array = np.linspace(0,T,N_t)

  csv_data = read_initial_conditions('initial_conditions.csv')
  C_current = interpolate_initial_conditions(csv_data,x_array)

  C_history = np.zeros((N_t,N_x))
  C_history[0,:] = C_current[:]

  source_history = np.zeros(N_t)
  source_history[0] = C0

  for n in range(1,N_T):
    current_time = n * Delta_t
    u = constant_velocity(U,N_x)
    A,B = compute_coefficients(u,Delta_t,Delta_x)

    if decay_rate == 0:
      C_source = C0

    else:
      C_source = decaying_source_concentration(C0,current_time,decay_rate)

    C_new = forward_substitution(A,B,C_current,left_bc=C_source)

    C_new[0] = C_source
    apply_outflow_boundary(C_new)

    C_current = C_new.copy()
    C_history[n,:] = C_current[:]
    source_history[n] = C_source
  return x_array,t_array,C_history,source_history 

L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 0.1
C0 = 250.0
decay_rate = 0.01

print("Running Task 10:Exponentially Decaying Source Team")
print(f"Decay rate λ = {decay_rate} s⁻¹")
print(f"Half-life = {np.log(2)/decay_rate:.1f} seconds")

print("\nRunning constant source simulation (baseline)")
x_const,t_const,C_const,source_const = run_simulation_with_source(decay_rate=0.0)

print("Running decaying source simulation")
x_decay,t_decay,C_decay,source_decay = run_simulation_with_source(decay_rate=decay_rate)

fig1,ax1 = plt.subplots(figsize=(10,6))
ax1.plot(t_const/60,source_const,'b-',linewidth=2,label='Constant source')
ax1.plot(t_decay/60,source_decay,'r-',linewidth=2,label=f'Decaying source (λ={decay_rate} s⁻¹)')
ax1.set_xlabel("Time(minutes)")
ax1.set_ylabel("Source concentration (μg/m³)")
ax1.set_title("Task 10: Source Concentration vs Time")
ax1.grid(True)
ax1.legend()
plt.tight_layout()
plt.savefig("results/task10_source_decay.png")
plt.show()

time_indices = [0,int(0.2 * len(t_decay)),int(0.5 * len(t_decay)),len(t_decay) - 1]
fig2,ax2 = plt.subplots(figsize=(12,7))

for i, n in enumerate(time_indices):
  time_min = t_decay[n] / 60 
  ax2.plot(x_const,C_const[n,:],'--',
           label=f't={time_min:.1f} min (constan)', alpha=0.7)
  ax2.plot(x_decay,C_decay[n,:],'-',
           label=f't={time_min:.1f} min (decaying)',linewidth=2)

ax2.set_xlabel("Distance along river (m)")
ax2.set_ylabel("Pollutant concentration (μg/m³)")
ax2.set_title("Task 10: Constant vs Decaying Source Comparison")
ax2.grid(True)
ax2.legend(loc='best',ncol=2)
plt.tight_layout()
plt.savefig("results/task10_comparison.png")
plt.show()

fig3,ax3 = plt.subplots(figsize=(10,6))

for n in time_indices:
  time_min = t_decay[n] / 60 
  difference = C_const[n,:] - C_decay[n,:]
  ax3.plot(x_decay,difference,label=f't={time_min:.1f} min')


ax3.set_xlabel("Distance along river (m)")
ax3.set_ylabel("Concentration difference (μg/m³)")
ax3.set_title("Task 10: Difference (Constant Source - Decaying Source)")
ax3.grid(True)
ax3.legend()
plt.tight_layout()
plt.savefig("results/task10_difference.png")
plt.show()

fig4,(ax4a,ax4b) = plt.subplots(1,2,figsize=(14,5))

im1 = ax4a.contourf(x_const,t_const / 60,C_const,levels=20,cmap='viridis')
ax4a.set_xlabel("Distance(m)")
ax4a.set_ylabel("Time(minutes)")
ax4a.set_title(Constant Source")
plt.colorbar(im1,ax=ax4a,label='Concentration (μg/m³)')

im2 = ax4b.contourf(x_decay, t_decay / 60, C_decay, levels=20, cmap='viridis')
ax4b.set_xlabel("Distance (m)")
ax4b.set_ylabel("Time (minutes)")
ax4b.set_title(f"Decaying Source (λ={decay_rate} s⁻¹)")
plt.colorbar(im2, ax=ax4b, label='Concentration (μg/m³)')

plt.tight_layout()
plt.savefig("results/task10_spacetime.png")
plt.show()

total_mass_const = np.trapz(C_const[-1, :], x_const)
total_mass_decay = np.trapz(C_decay[-1, :], x_decay)
mass_reduction = (total_mass_const - total_mass_decay) / total_mass_const * 100

print(f"\n=== Task 10 Analysis ===")
print(f"Final source concentration (constant): {source_const[-1]:.2f} μg/m³")
print(f"Final source concentration (decaying): {source_decay[-1]:.2f} μg/m³")
print(f"Source reduction: {(1 - source_decay[-1]/source_const[-1])*100:.1f}%")
print(f"\nIntegrated pollutant mass at t={T/60:.1f} min:")
print(f"  Constant source: {total_mass_const:.2f} μg·m/m³")
print(f"  Decaying source: {total_mass_decay:.2f} μg·m/m³")
print(f"  Mass reduction: {mass_reduction:.1f}%")
print(f"\nAll plots saved to results/ directory")
print("Task 10 Complete!")
