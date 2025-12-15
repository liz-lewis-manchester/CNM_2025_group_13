def apply_inflow_boundary(C_next: np.ndarray, current_time: float, U: float) -> None:
    """Applies the Dirichlet boundary condition at x=0."""
    SOURCE_CONCENTRATION = 250.0 # µg/m³
    if current_time >= 0:
        C_next[0] = SOURCE_CONCENTRATION
def apply_outflow_boundary(C_next: np.ndarray) -> None:
    """Applies a zero-gradient (Neumann) boundary condition at x=L."""
    last_index = len(C_next) - 1
    C_next[last_index] = C_next[last_index - 1]
for t_step in range(Nt):
    apply_inflow_boundary(C_next, current_time, U) 
    apply_outflow_boundary(C_next)
