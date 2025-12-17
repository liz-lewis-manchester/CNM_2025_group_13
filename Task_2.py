#Task 2: storage of matrix 
import numpy as np 
#Creating placeholders for the coefficients A and B
A=np.zeros((N_x-1))
B=np.zeros((N_x-1))

#Setting up the code to work in both positive and negative directiob
if U > 0:
  a= (1/Delta_t) + (U/Delta_x) 
  b= -U/Delta_x
else: 
  a= (1/Delta_t) - (U/Delta_x)
  b= U/Delta_x 

#Setting up the coefficients as constants within the domain as U is constant
A[:]=a
B[:]=b
