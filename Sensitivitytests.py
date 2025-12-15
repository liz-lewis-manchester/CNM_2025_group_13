import numpy as np 
import matplotlib.pyplot as plt 
from src.code import read_intial_conditions 
from src.interp import interpolate_intial_conditions
from src.solver import forward_substitution
from src.boundary import apply_inflow_boundary, apply_outflow_boundary 
from src.coefficients import compute_coefficients 
from src.velocity import constant_velocity 
import os 

def run_simulation(U,Delta_x,Delta_t,L=20.0,T=300.0,C0=250.0):
  """run simulation with gven parameters and return final state""" 
  N_x = int(L/Delta_x) + 1
  N_t = int(T/Delta_t) + 1
  x_array = np.linspace(0,L,N_x)

  csv_data = read_initial_conditions('initial_conditions.csv')
  C_current = interpolate_initial_conditions(csv_data,x_array)

  for n in range(1,N_t):
    u = constant_velocity(U,N_x)
    A,B = compute_coefficients(u,Delta_t,Delta_x)
    C_new = forward_substitution(A,B,C_current,left_bc=C0)

    current_time = n * Delta_t
    apply_inflow_boundary(C_new,current_time,U)
    apply_outflow_boundary(C_new)
    C_current = C_new.copy()

  return x_array,C_current 

os.makedirs('results',exist_ok=True)

T = 5.0 * 60.0 
L = 20.0
Delta_x_base = 0.2
Delta_t_base = 10.0
U_base = 0.1
C0 = 250.0

print("Running baseline simulation")
x_base,C_base = run_simulation(U_base,Delta_x_base,Delta_t_base)

print("\nRunning velocity sensitivity tests")
velocities = [0.05,0.1,0.2]
fig1,ax1 = plt.subplots(figsize=(10,6))
ax1.plot(x_base,C_base,'K--",linewidth=2,label = f'Baseline U={U_base} m/s')

for U in velocities:
  if U!=U_base:
     x,C = run_simulation(U,Delta_x_base,Delta_t_base)
     ax1.plot(x,C,label=f'U={U} m/s')
     diff = np.max(np.abs(C - np.interp(x,x_base,C_base)))
     print(f"U={U} m/s: Max difference from baseline = {diff:.2f} μg/m³")

ax1.set_xlabel("Distance along river (m)")
ax1.set_ylabel("Pollutant concentration (μg/m³)")
ax1.set_title("Task 9: Velocity Sensitivity Test")
ax1.grid(True)
ax1.legend()
plt.tight_layout()
plt.savefig("results/task9_velocity_sensitivity.png")
plt.show()

print("\nRunning spatial resolution sensitivity tests")
delta_x_values = [0.1,0.2,0.4]
fig2, ax2 = plt.subplots(figsize=(10,6))

for dx in delta_x_values:
   x,C = run_simulation(U_base, dx, Delta_t_base)
   label = f'Δx={dx} m' + ('(Baseline)' if dx ==Delta_x_base else '')
   style = 'k--' if dx ==Delta_x_base else '-'
   linewidth = 2 if dx ==Delta_x_base else 1
   ax2.plot(x,C,style,linewidth=linewidth,label=label)
   print(f"Δx={dx} m: Grid points = {len(x)}")

ax2.set_xlabel("Distance along river (m)")
ax2.set_ylabel("Poluutant concentration (μg/m³)")
ax2.set_title("Task 9: Spatial Resolution Sensitivity Test")
ax2.grid(True)
ax2.legend()
plt.tight_layout()
plt.savefig("results/task9_spatial_sensitivity.png")
plt.show()

print("\nRunning temporal resolution sensitivity tests")
delta_t_values = [5.0,10.0,20.0]
fig3,ax3 = plt.subplots(figsize=(10,6))

for dt in delta_t_values:
   x,C = run_simulation(U_base,Delta_x_base,dt)
   label = f'Δt={dt} s' + (' (Baseline)' if dt == Delta_t_base else '')
   style = 'k--' if dt == Delta_t_base else '-'
   linewidth = 2 if dt == Delta_t_base else 1
   ax3.plot(x,C,style,linewidth=linewidth,label=label)
   diff = np.max(np.abs(C - C_base))
   print(f"Δt={dt} s: Max difference from baseline = {diff:.2f} μg/m³")

ax3.set_xlabel("Distance along river (m)")
ax3.set_ylabel("Pollutant concentration (μg/m³)")
ax3.set_title("Task 9: Temporal Resolution Sensitivity Test")
ax3.grid(True)
ax3.legend()
plt.tight_layout()
plt.savefig("results/task9_temporal_sensitivity.png")
plt.show()

print("\nGenerating combined comparison plot")
fig4, (ax4a, ax4b, ax4c) = plt.subplots(3, 1, figsize=(10,12))

for U in velocities:
   x,C = run_simulation(U, Delta_x_base, Delta_t_base)
   diff = C - np.interp(x, x_base, C_base)
   ax4a.plot(x, diff, label=f'U={U} m/s')
ax4a.set_ylabel("Concentration difference (μg/m³)")
ax4a.set_title("Differences in Pollutant Spread: Velocity Variation")
ax4a.grid(True)
ax4a.legend()

for dx in delta_x_values:
   if dx !=Delta_x_base:
       x,C = run_simulation(U_base, dx, Delta_t_base)
       C_interp = np.interp(x, x_base, C_base)
       diff = C - C_interp
       ax4b.plot(x, diff, label=f'Δx={dx} m')
ax4b.set_ylabel("Concentration difference  (μg/m³)")
ax4b.set_title("Differences in Pollutant Spread: Temporal Resolution")
ax4b.grid(True)
ax4b.legend()

for dt in delta_t_values:
    if dt != Delta_t_base:
        x, C = run_simulation(U_base, Delta_x_base, dt)
        diff = C - C_base
        ax4c.plot(x, diff, label=f'Δt={dt} s')
ax4c.set_xlabel("Distance along river (m)")
ax4c.set_ylabel("Concentration difference (μg/m³)")
ax4c.set_title("Differences in Pollutant Spread: Temporal Resolution")
ax4c.grid(True)
ax4c.legend()

plt.tight_layout()
plt.savefig("results/task9_all_differences.png")
plt.show()

print("\n" + "="*60)
print("Task 9 Complete!")
print("="*60)
print("\nGenerated files:")
print(" -results/task9_velocity_sensitivity.png")
print(" -results/task9_spatial_sensitivity.png")
print(" -results/task9_temporal_sensitivity.png")
print(" -results/task9_all_differences.png")
print("\nAll sensitivity test plots saved to results/")
