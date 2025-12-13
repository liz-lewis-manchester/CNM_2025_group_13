Import numpy as np 
A=np.zeros((N_x-1))
B=np.zeros((N_x-1))
O_old=np.zeros((N_x))
O_new=np.zeros((N_x))

a= (1/Delta_t) + (U/Delta_x)
b= -U/Delta_x

A[:]=a
B[:]=b
