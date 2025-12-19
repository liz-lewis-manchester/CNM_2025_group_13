import numpy as np

def setup_domain(L, T, Delta_x, Delta_t):
  N_x = int(L / Delta_X) + 1
  N_t = int(T / Delta_t) + 1
  x_array = np.linspace(0, L, N_x)
  t_array = np.linspace(0, T, N_t)

  return x_array, t_array, N_x, N_t

def initial_conditions(N_x, C0, start_index=0):
  C_current = np.zeros(N_x)
  C_next = C_current.copy()
  C_current[start_index] = C0

  return C_current, C_next

L = 20.0
T = 5.0 * 60.0
Delta_x = 0.2
Delta_t = 10.0
U = 10.0
C0 = 250.0
x_array, t_array, N_x, N_t = setup_domain(L, T, Delta_x, Delta_t)
C_history = np.zeros((N_t, N_x))
C_current, C_next = intial_conditions(N_x, C0, start_index=0)
C_history[0, :] = C_current[:]

