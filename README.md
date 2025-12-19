### Task 12 — Plotting & Visualisation

Task 12 introduces reusable plotting utilities to visualise pollutant concentration results.

- Snapshot plots of concentration vs. distance at selected timesteps
- Time evolution plots comparing concentration profiles over time
- All figures are automatically saved to the `results/` directory

**Files added/updated:**
src/plotting.py

Plots are generated automatically when running the simulation.

---

### Task 13 — Automated Testing

Task 13 adds automated testing using `pytest` to ensure correctness and reproducibility.

Implemented tests include:
- Interpolation correctness
- Solver functionality
- Boundary condition handling
- Plotting functions execution
- Small integration test to verify full model execution

**Tests added:**
tests/
test_interpolation.py
test_solver.py
test_boundary.py
test_plotting.py
test_full_run.py

Run tests with:
```bash
pytest
