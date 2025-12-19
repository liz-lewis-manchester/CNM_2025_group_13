# CNM_2025_group_13

Overview
-
This repository contains a Python code that using numerical method it simulates the evolution of a pollutant concentration in a river. The aim is to model how pollutant concentration envolves over time and distance, by using the the advection equation: 

<img width="179" height="85" alt="image" src="https://github.com/user-attachments/assets/8281aba8-f7db-43a4-af10-e921480e3941" />


where:
	
	θ = C pollutant concentration (µg/m³)
	
	t = time (s)
	
	x = distance along the river (m)
	
	U = velocity (ms-1)

The code is flexible, allowing the user to change parameters, and it will automatically generate a graphical outputs for visualisation.

Repository Structure
-
 /CNM_2025_group_13


 - Doc/

       - milestones.md  #File with the milestones and tasks

 - Notebooks/ #Notebooks where the code was ran to check if it worked
   
       - Copy_of_Test_Task1_Domain.ipynb
       - Task_7_Test_1_BaselineSimulation(1).ipynb
       - Test_Tast2_StorageOfMatrix(2).ipynb
       - Test_Task3_ForwardSubstitution.ipynb
       - Test_Task5and6.ipynb

 - Tests/
   
       - TestBoundary.py
       - TestDomain.py
       - TestSolver.py
      
 - data/
   
       - initial_conditions.csv #File from initial condition
   
 - src/
   
       - _iniy_.py   #Empty file that allows the folder to be read by colab
       - boundary.py #Task 4
       - domain.py #Task1,5 and 9
       - solver.py #Tasks 3 and 4
       - plotting.py #Task 12

 - README.md

Milestones and Tasks
-
**Milestone 1:Setup**
- Task 1: Model domain and initialisation of grid
- Task 2: Splitting matrix into coefficient A and B
- Task 3: Forward substitution solver

**Milestone 2:Boundary Conditions**
- Task 4: Create boundary condition
- Task 5: Reading initial_conditions.csv
- Task 6: Interpolating initial condition with model grid

**Milestone 3:Simulations**
- Task 7: Baseline simulation
- Task 8: Simulation with the initial conditions are read in from a csv file ‘initial_conditions.csv 

**Milestone 4:Tests**
- Task 9: Sensitivity test (U, spatial and temporal resolution)
- Task 10: Exponetial decay in time
- Task 11: Variable stream velocity profile

**Milestone 5: Visualisation and Vlidation**
- Task 12: Plotting & Visualisation Tools
- Task 13: Automated Tests

They are futher described in the docs/ folder


How to run the Code
-
- Copy the repository with !git clone https://github.com/liz-lewis-manchester/CNM_2025_group_13.git, and import all the function needed (e.g from src.solver import storing_matrix, forward_substitution)
- Define parameters: L, T, Delta_x, Delta_t, U, C0
- Initialise domain: x_array, t_array, N_x, N_t = setup_domain(L, T, Delta_x, Delta_t) and C_current, C_next = initial_conditions(N_x, initial_value, start_index=0)
- A,B= storing_matrix(N_x, Delta_t, Delta_x, U)
- Placeholders need to be created: C_history = np.zeros((N_t, N_x)) and C_history[0,:]= C_current
- For n in range (1,N_t): F=(1/Delta_t)*C_current[1:] C_next= forward_substitution(A, B, F, C_next) C_current[:]=C_next[:]
- Apply outflow and inflow function inside the loop
- Just plot the graph

Authors
-
**CNM_2025_group_13**
- Kataryna Santana Couto
- Muhammad Ramlee
- William Gardiner
- Zina Almazloum
- Hon Wong 
-
