# CNM_2025_group_13
#Setup Domain
This part sets up the models domain

# Initial Conditions
This part of the code is responsible for defining the intial conditions for the model

# Defining Variables
This part sets the values for the variables in the model

Task 3: Forward Substitution
-
This branch focus on creating a code to solve the forward substitution. 
How to use this section of the code:
- Define parameters: L, T, Delta_x, Delta_t, U, C0
- Initialise domain: x_array, t_array, N_x, N_t = setup_domain(L, T, Delta_x, Delta_t) and 
C_current, C_next = initial_conditions(N_x, initial_value, start_index=0)
- A,B= storing_matrix(N_x, Delta_t, Delta_x, U)
- For n in range (1,N_t):
  F=(1/Delta_t)*C_current[1:]
  C_next= forward_substitution(A, B, F, C_next)
  C_current[:]=C_next[:]
