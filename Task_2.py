import numpy as np 
A=np.zeros((N_x-1))
B=np.zeros((N_x-1))
theta_old=np.zeros((N_x))
theta_new=np.zeros((N_x))

if U > 0:
  a= (1/Delta_t) + (U/Delta_x)
  b= -U/Delta_x
else: 
  a= (1/Delta_t) - (U/Delta_x)
  b= U/Delta_x 

A[:]=a
B[:]=b
