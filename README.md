# CNM_2025_group_13

Overview
-
This repository contains a Python code that using numerical method it simulates the evolution of a pollutant concentration in a river. The aim is to model how pollutant concentration envolves over time and distance, by using the the advection equation: 



where:
	θ = pollutant concentration (µg/m³)
	t = time (s)
	x = distance along the river (m)
	U = velocity (ms-1)

The code is flexible, allowing the user to change parameters, and it will automatically generate a graphical outputs for visualisation.

Repository Structure
-


Milestones and Tasks
-
- *Milestone 1:Setup*
  -Task 1: Model domain and initialisation of grid
  -Task 2: Splitting matrix into coefficient A and B
  -Task 3: Forward substitution solver

- *Milestone 2:Boundary Conditions*
  -Task 4: Create boundary condition
  -Task 5: Reading initial_conditions.csv
  -Task 6: Interpolating initial condition with model grid

- *Milestone 3:Simulations*
-Task 7: Baseline simulation 
-Task 8: Simulation with the initial conditions are read in from a csv file ‘initial_conditions.csv 

- *Milestone 4:Tests*
  -Task 9: Sensitivity test (U, spatial and temporal resolution)
  -Task 10: Exponetial decay in time 
  -Task 11: Variable stream velocity profile 
  
They are futher described in the docs/ folder


How to run the Code
-
1- Copy the repository with !git clone https://github.com/liz-lewis-manchester/CNM_2025_group_13.git

Authors
-
CNM_2025_group_13
-

