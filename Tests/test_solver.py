import numpy as np
from src.solver import forward_substitution

def test_forward_substitution():
    A = np.ones(5)
    B = np.array([-0.1] * 5)
    C_old = np.array([1,2,3,4,5], float)

    C_new = forward_substitution(A, B, C_old, left_bc=1)

    assert C_new[0] == 1
    assert len(C_new) == 5
