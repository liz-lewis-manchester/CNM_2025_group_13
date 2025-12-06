# CNM_2025_group_13
F=(1/dt)*O_old[1:] #Setting up right hand side vecto F 

def forward_substitution(A, B, F, O): #defining a function to solve the linear system 
  NX= len(F) +1 #Total grid points, as F is one shorter than O_old
  O_new= np.zeros ((NX)) #Creating solution vector
  O_new[0]=O #Adding boundary condition at x=0
  
  for i in range (1,NX): #Creating a loop to solve the linear system 
    O_new[i]=(1/(A[i-1]))*(F[i-1]- B[i-1]*O_new[i-1])

  return O_new #Setting up the return of the Θ_new from this function
