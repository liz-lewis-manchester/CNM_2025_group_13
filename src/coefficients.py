import numpy as np

def compute_coefficients(u, dt, dx):
    Nx = len(u)
    A = np.ones(Nx)
    B = -u * dt / dx
    return A, B
