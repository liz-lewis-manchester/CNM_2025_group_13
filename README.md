# CNM_2025_group_13

Task 2: Storage of matrix
-
This branch focus on creating coefficients A and B for the matrix, for later use in solving the equation.

How to use this section of the code: 
- Define parameters: L, T, Delta_x, Delta_t, U, C0
- Initialise domain: x_array, t_array, N_x, N_t = setup_domain(L, T, Delta_x, Delta_t) and C_current, C_next = initial_conditions(N_x, initial_value, start_index=0)
- A,B= storing_matrix(N_x, Delta_t, Delta_x, U)
