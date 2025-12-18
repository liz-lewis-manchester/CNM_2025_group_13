# CNM_2025_group_13
#Task 3
#F=(1/Delta_t)*C_current[1:] #Setting up right hand side vector F 

def forward_substitution(A, B, F, C_next): #defining a function to solve the linear system 
  N_x= len(F) +1 #Total grid points, as F is one shorter than C_current
 
  
  for i in range (1,N_x): #Creating a loop to solve the linear system 
    C_next[i]=(1/(A[i-1]))*(F[i-1]- B[i-1]*C_next[i-1])

  return C_next #Setting up the return of the C_next from this function
