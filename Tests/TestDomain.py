#Automated test for domain

#Checking if the value obtained matches the equation
assert N_x == int(L / Delta_x) + 1
assert N_t == int(T / Delta_t) + 1

#Checking if the grid atarts at 0 and finishes at L and T
assert x_array[0] == 0.0
assert L==(x_array[-1])
assert t_array[0] == 0.0
assert T==(t_array[-1])

#Checking initial conditions 
assert C_current[0] == C0
assert np.all(C_current[1:] == 0)
