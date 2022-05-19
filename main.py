
import sys
import math

#Physical parameters

P = 0.2 #Length of the effector platform
Cx = 0 #X coord of the left shoulder
Cy = 0 #Y coord of the left shoulder
lb = 1 #Length of the upper half of the arm
la = 1 #Length of the lower half of the arm
D = 1.5 #Distance between shoulders


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
    
    if not mode:
        leftAngle = math.radians(leftAngle)
        rightAngle = math.radians(rightAngle)
    return [leftAngle, rightAngle]

def initialCalculations(angles = []):
    #Get the params if they haven't been provided
    if not angles:
        angles = getInput()
    
    #X coord of the end of the upper half of the left arm
    Xl = lb * math.cos(angles[0])
    
    #X coord of the end of the upper half of the right arm
    Xr = lb * math.cos(angles[1]) 
    
    #Y coord of the end of the upper half of the left arm
    Yl = lb * math.sin(angles[0])
    
    #Y coord of the end of the upper half of the right arm
    Yr = lb * math.sin(angles[1])
    
    #Auxiliary variables
    
    Aux1 = Xl + P - D - 2 * Xr 
    Aux2 = Yl - 2 * Yr * Yr
    Aux3 = D + Xr - P - 2 * Xl
    Aux4 = Yr - 2 * Yl
    
    #Purely calculational variables

    A = - 2 * (Xl + Aux1)
    B = - 2 * (Yl + Aux2)
    N = - 2 * (Xr + Aux3)
    U = - 2 * (Yr + Aux4)
    I = Aux1 * Aux1 + Aux2 * Aux2 - Xl * Xl - Yl * Yl
    O = D + Xr - P - Xl
    E = Yr - Yl
    #IMPORTANT: This variable is in no way related to coordinates
    X = Aux3 * Aux3 + Aux4 * Aux4 - Xr * Xr - Yr * Yr
    
    return [A, B, N, U, I, O, E, X, Xl, Yl, Xr, Yr]

#Main and final calculations
def mainCalculations(coordsAndParams = []):
    #Get the params if they haven't been provided
    if not coordsAndParams:
        coordsAndParams = initialCalculations()
    
    #Unpacking variables
    A = coordsAndParams[0]
    B = coordsAndParams[1]
    N = coordsAndParams[2]
    U = coordsAndParams[3]
    I = coordsAndParams[4]
    O = coordsAndParams[5]
    E = coordsAndParams[6]
    X = coordsAndParams[7]
    
    Xl = coordsAndParams[8]
    Yl = coordsAndParams[9]
    Xr = coordsAndParams[10]
    Yr = coordsAndParams[11]
    
    #Auxiliary variable calculations
    
    auxNOUE = X + N * O + U * E
    
    denominator = A * U - B * N
    numeratorA1 = I * U - B * auxNOUE 
    numeratorB1 = A * auxNOUE - I * N
    numeratorA2 = I * U - U * O * A - B * (X + U * E)
    numeratorB2 = A * (N * O + X) + B * N * E - I * N
    
    #Actual calculations according to some predefined equations
    a1 = numeratorA1/denominator
    b1 = numeratorB1/denominator
    a2 = numeratorA2/denominator
    b2 = numeratorB2/denominator
    
    #Final position calculations
    finalX1 = a1 + Xl
    finalY1 = b1 + Yl
    finalX2 = a2 + Xr
    finalY2 = b2 + Yr
    
    
    return [finalX1, finalY1, finalX2, finalY2]

print(mainCalculations())