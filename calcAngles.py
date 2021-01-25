
import math
def computeAngles(x, y):
    x = x* 1.000000000
    y = y * 1.000000000
    print("x,y", x, y)
    if(x** 2 + y**2 > 4) :
        normalizingFactor = math.sqrt((3.999)/(x** 2 + y**2))
        print(normalizingFactor)
        x = x * normalizingFactor
        y = y * normalizingFactor

    sumsq = (y ** 2 + x ** 2)
    cosdiff = (sumsq - 2)/2
    b = math.acos(cosdiff)
    sindiff = math.sin(b)

    numerator = y * (1 + cosdiff) - x * sindiff
    denominator = (0.000001 + sindiff ** 2 + (1 + cosdiff) ** 2)
    sinb = numerator / denominator
    a = math.asin(sinb)
    return ((a * 180)/math.pi,(b * 180)/math.pi)
