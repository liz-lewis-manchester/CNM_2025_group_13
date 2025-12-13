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
  run simulation with gven parameters and return final state 
  N_x = int(L/Delta_x) + 1
  N_t = int(T/Delta_t) + 1
  x_array = np.linspace(0,L,N_x)

  csv_data = read_intial_consitions('intial_consitions.csv')
  C_current = interpolater_initial_conditions(csv_data,x_array)

  for n in range(1,N_t):
    u = constant_velocity(U,N_x)
    A,B = compute_coefficients(u,Delta_t,Delta_x)
    C_new = forward_substitution(A,B,C_current,left_bc=C0)

    current_time = n * Delta_t
    apply_inflow_boundary(C_new,current_time,U)
    apply_outflow_boundary(C_new)
    C_current = C_new.compy()

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
     x,C 
