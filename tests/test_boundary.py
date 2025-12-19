import numpy as np
from src.boundary import apply_left_boundary, apply_right_boundary

def test_left_boundary():
    C = np.zeros(5)
    out = apply_left_boundary(C, 99)
    assert out[0] == 99

def test_right_boundary():
    C = np.array([1,2,3,4,5], float)
    out = apply_right_boundary(C)
    assert out[-1] == out[-2]
