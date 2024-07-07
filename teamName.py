import numpy as np

##### TODO #########################################
### RENAME THIS FILE TO YOUR TEAM NAME #############
### IMPLEMENT 'getMyPosition' FUNCTION #############
### TO RUN, RUN 'eval.py' ##########################

nInst = 50
currentPos = np.zeros(nInst)


## prcSoFar is a 2D array

def getMyPosition(prcSoFar):
    global currentPos
    # get dimension of the matrix (returns touple with rows and cols)
    (nins, nt) = prcSoFar.shape
    if (nt < 2):
        return np.zeros(nins)
    # gets percentage change in natural log form much better for finance crap
    lastRet = np.log(prcSoFar[:, -1] / prcSoFar[:, -2])
    makeSureDoingWell = np.log(prcSoFar[:, -1] / prcSoFar[:, -nt])
    lastRet = lastRet + makeSureDoingWell

    # normalise
    lNorm = np.sqrt(lastRet.dot(lastRet))
    lastRet /= lNorm

    # new position
    rpos = np.array([int(x) for x in 5000 * lastRet / prcSoFar[:, -1]])


    currentPos = np.array([int(x) for x in currentPos+rpos])
    return currentPos
