import numpy as np

def constant_velocity(u0, Nx):
    return np.full(Nx, u0)


def noisy_velocity(u0, Nx, noise=0.10, seed=42):
    """Spatially varying velocity (±10%)."""
    rng = np.random.default_rng(seed)
    return u0 * (1 + noise * rng.standard_normal(Nx))


def time_varying_velocity(u0, Nx, step, noise=0.10):
    """Velocity varies each timestep."""
    rng = np.random.default_rng(step)
    return u0 * (1 + noise * rng.standard_normal(Nx))
