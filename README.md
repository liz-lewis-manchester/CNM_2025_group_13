# CNM_2025_group_13
F=(1/Delta_t)*0_old[1:] #Setting up right hand side vecto F 

def forward_substitution(A, B, F, 0): #defining a function to solve the linear system 
  N_x= len(F) +1 #Total grid points, as F is one shorter than 0_old
  0_new= np.zeros ((N_x)) #Creating solution vector
  0_new[0]=0 #Adding boundary condition at x=0
  
  for i in range (1,N_x): #Creating a loop to solve the linear system 
    0_new[i]=(1/(A[i-1]))*(F[i-1]- B[i-1]*0_new[i-1])

  return 0_new #Setting up the return of the Θ_new from this function
