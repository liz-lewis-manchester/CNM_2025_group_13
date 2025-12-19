from src.velocity import time_varying_velocity

def test_time_varying_velocity():
    v = time_varying_velocity(0.1, 10, step=1)
    assert len(v) == 10
