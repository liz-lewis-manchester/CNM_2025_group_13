for step in range(1, Nt):

    # Variable velocity (Task 11)
    u = time_varying_velocity(u0, Nx, step)

    A, B = compute_coefficients(u, dt, dx)

    C_new = forward_substitution(A, B, C_old, left_bc=C_old[0])

    C_old = C_new.copy()
    C_hist.append(C_old)
