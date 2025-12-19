import numpy as np
from src.interp import interpolate_initial_conditions

def test_interpolation():
    x  = np.array([0, 10, 20])
    c  = np.array([0, 5, 10])
    grid = np.array([0, 5, 10, 15, 20])

    result = interpolate_initial_conditions(x, c, grid)

    assert np.allclose(result, [0, 2.5, 5, 7.5, 10])
