
import sys
import math

#Physical parameters

P = 0 #Length of the effector platform
Cx = 0 #X coord of the left shoulder
Cy = 0 #Y coord of the left shoulder
lb = 0 #Length of the upper half of the arm
la = 0 #Length of the lower half of the arm
D = 0 #Distance between shoulders


#Gets the unit in which the input will be given
def getUnit():
    unit = input("Select the unit for angles (d/r): ")
    if unit == "d":
        return 0
    elif unit == "r":
        return 1
    else:
        return getUnit()

#Gets the input angles from the user
def getInput(mode = sys.maxsize):
    #Get the params if they haven't been provided
    if mode > 1:
        mode = getUnit()
    auxText = ["(degrees)", "(radians)"]
    leftAngle = float(input("Insert the angle of the left motor " + auxText[mode]))
    rightAngle = float(input("Insert the angle of the right motor " + auxText[mode]))
    return [leftAngle, rightAngle]

def initialCalculations(angles = []):
    #Get the params if they haven't been provided
    if not angles:
        angles = getInput()
    
    #X coord of the end of the upper half of the left arm
    Xl = 0 
    
    #X coord of the end of the upper half of the right arm
    Xr = 0 
    
    #Y coord of the end of the upper half of the left arm
    Yl = 0 
    
    #Y coord of the end of the upper half of the right arm
    Yr = 0
    
    #Purely calculational variables

    A = 2 * (-2 * Xl - P + D + 2 * Xr)
    W = 4 * (Yr - Yl)
    U = 2 * (-2 * Xr + 2 * Xl + P - D)
    T = -3 * Yl - Yr
    I = D * D + P * P + 3 * (Xr * Xr + Yr * Yr) + Xl * Xl + Yl * Yl + 2 * (-2 * Xr * P - Xl * D - P * D + P * Xl - 2 * Xr * Xl + 2 * Xr * D)
    E = 0
    V = 0
    N = 0
    
    return [A, W, U, T, I, E, V, N]

#Main and final calculations
def mainCalculations(coordsAndParams = []):
    #Get the params if they haven't been provided
    if not coordsAndParams:
        coordsAndParams = initialCalculations()
    
    #Unpacking variables
    A = coordsAndParams[0]
    W = coordsAndParams[1]
    U = coordsAndParams[2]
    T = coordsAndParams[3]
    I = coordsAndParams[4]
    E = coordsAndParams[5]
    V = coordsAndParams[6]
    N = coordsAndParams[7]
    
    #Auxiliary variable calculations
    auxA = (W *  E) + (W * T * V) - (T * I)
    auxB = (I * U) - (A * E) - (A * U * N)
    auxDenominator = (W * U) - (A * T)
    auxNumeratorA1 = (W * U * N) + auxA
    auxNumeratorB1 = auxB - (A * T * V)
    auxNumeratorA2 = (A * T * N) + auxA
    auxNumeratorB2 = auxB - (W * U * V)
    
    #Actual calculations according to some predefined equations
    a1 = auxNumeratorA1/auxDenominator
    b1 = auxNumeratorB1/auxDenominator
    a2 = auxNumeratorA2/auxDenominator
    b2 = auxNumeratorB2/auxDenominator

    return [a1, b1, a2, b2]