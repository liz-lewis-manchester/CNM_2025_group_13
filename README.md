# CNM_2025_group_13
Import numpy as np 
A=np.zeros((NX-1))
B=np.zeros((NX-1))
O_old=np.zeros((NX))
O_new=np.zeros((NX))

a= (1/dt) + (u/dx)
b= -u/dx

A[:]=a
B[:]=b
