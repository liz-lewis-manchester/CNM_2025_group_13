from src.run_simulation import run_simulation

def test_full_run():
    x, t, C = run_simulation(L=2, dx=1, T=10, dt=5)

    assert C.shape[0] == len(t)
    assert C.shape[1] == len(x)
