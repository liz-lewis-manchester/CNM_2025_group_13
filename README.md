import numpy as np

def constant_velocity(u0, Nx):
    return np.full(Nx, u0)

def velocity_with_random_noise(u0, Nx, noise_level=0.1, seed=42):
    rng = np.random.default_rng(seed)
    perturb = 1 + noise_level * rng.standard_normal(Nx)
    return u0 * perturb

def time_varying_velocity(u0, Nx, t, noise_level=0.1):
    """Example: velocity changes 1% every timestep."""
    rng = np.random.default_rng(int(t))
    return u0 * (1 + noise_level * rng.standard_normal(Nx))
