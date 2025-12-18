#Automated test for solver.py

#Test for storage of matrix 
# Checking length
assert len(A) == N_x - 1
assert len(B) == N_x - 1

# Chcking if A and B are constant
assert np.allclose(A, A[0])
assert np.allclose(B, B[0])

#Test for Forward substitution 
#e is the expected result from a manual calculation
e = np.zeros(N_x) #placeholder
e[0] = 1.0  #setting up the first number of e 
for i in range(1, N_x):   #checking if all the numbers are the same in the forward substitution 
    e[i] = (1 - (-1) * e[i-1]) / 2

np.allclose(C_next, e)


