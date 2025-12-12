def apply_inflow_boundary(theta_new: np.ndarray, current_time: float, U: float) -> None:
    """Applies the Dirichlet boundary condition at x=0."""
    SOURCE_CONCENTRATION = 250.0 # µg/m³
    if current_time >= 0:
        theta_new[0] = SOURCE_CONCENTRATION
def apply_outflow_boundary(theta_new: np.ndarray) -> None:
    """Applies a zero-gradient (Neumann) boundary condition at x=L."""
    last_index = len(theta_new) - 1
    theta_new[last_index] = theta_new[last_index - 1]
for t_step in range(Nt):
    apply_inflow_boundary(theta_new, current_time, U) 
    apply_outflow_boundary(theta_new)
