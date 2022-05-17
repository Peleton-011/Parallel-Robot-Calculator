
import math

#Physical parameters

P = 0 #Length of the effector platform
Cx = 0 #X coord of the left shoulder
Cy = 0 #Y coord of the left shoulder
lb = 0 #Length of the upper half of the arm
la = 0 #Length of the lower half of the arm
D = 0 #Distance between shoulders

#Purely calculational variables

A = 0
W = 0
U = 0
T = 0
I = 0
E = 0
V = 0
N = 0

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
def getInput():
    mode = getUnit()
    auxText = ["(degrees)", "(radians)"]
    leftAngle = float(input("Insert the angle of the left motor " + auxText[mode]))
    rightAngle = float(input("Insert the angle of the right motor " + auxText[mode]))
    return [leftAngle, rightAngle]

def initialCalculations():
    angles = getInput()
    
    #X coord of the end of the upper half of the left arm
    Xl = 0 
    
    #X coord of the end of the upper half of the right arm
    Xr = 0 
    
    #Y coord of the end of the upper half of the left arm
    Yl = 0 
    
    #Y coord of the end of the upper half of the right arm
    Yr = 0 

    