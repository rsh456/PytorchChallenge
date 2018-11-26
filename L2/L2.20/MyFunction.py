import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    res = 0
    for i in range(len(Y)):
       pi=P[i]
       yi=Y[i]
       res1 = yi*np.log(pi)+(1-yi)*np.log(1-pi)
       res=res1+res
       
    return res*(-1)
    pass