import numpy as np

matrix = [[0.5,0.5,0],[0.5,0,0.5],[0.5,0,0.5]]

#Switch up matrix so that we cycle on the value that we want to predict first time until we enter
matrix = [[0.5,0.5,0],[0.5,0,0.5],[0,0,1]]

runprog = True
condition = [np.longdouble(1),np.longdouble(0),np.longdouble(0)]
estimate = np.longdouble(0)
prevprob =np.longdouble(0)
iter = np.longdouble(0)
np.longdouble
while(runprog):
    #Calculate new condition
    #
    estimate += iter*(condition[2]-prevprob)
    if(condition[2]-prevprob < np.longdouble(0.000000000000000001) and iter > 10):
        runprog = False
    prevprob = condition[2]
    iter += 1
    condition = np.dot(condition, matrix)
        
print(estimate)
