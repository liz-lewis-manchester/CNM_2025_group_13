# CNM_2025_group_13
#Task 3
F=(1/Delta_t)*theta_old[1:] #Setting up right hand side vector F 

def forward_substitution(A, B, F): #defining a function to solve the linear system 
  N_x= len(F) +1 #Total grid points, as F is one shorter than theta_old
  theta_new= np.zeros ((N_x)) #Creating solution vector
  theta_new[0]=0 #Adding boundary condition at x=0
  
  for i in range (1,N_x): #Creating a loop to solve the linear system 
    theta_new[i]=(1/(A[i-1]))*(F[i-1]- B[i-1]*theta_new[i-1])

  return theta_new #Setting up the return of the theta_new from this function
