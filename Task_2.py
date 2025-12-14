import numpy as np 
A=np.zeros((N_x-1))
B=np.zeros((N_x-1))
C_current=np.zeros((N_x))
C_next=np.zeros((N_x))

if U > 0:
  a= (1/Delta_t) + (U/Delta_x)
  b= -U/Delta_x
else: 
  a= (1/Delta_t) - (U/Delta_x)
  b= U/Delta_x 

A[:]=a
B[:]=b
