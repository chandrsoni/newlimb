
# First method(direct compute)
# y = l* sin(a) + l * sin(b)
# x = l * cos(a) + l * cos(b)
# x ** 2 + y** 2 <= 4 * l ** 2
#  0 < a < b < 180 
# square the first 2 equations and do sum of those
# (y*2 + x*2)/ l*2 = 2 + 2 *(cos(a-b))
# y/l = sinb * ( 1 + cosdiff) + cosb * (sindiff)
# x/l = cosb * ( 1 + cosdiff) - sinb * (sindiff)
# sinb =  y/l - ((x/l) * (sindiff/ (1 + cosdiff))) / (((1 + cosdiff) + sindiff * (sindiff/ (1 + cosdiff))))
# l * sinb = (y * (1 + cosdiff) - x * sindiff)/(sindiff ** 2 + (1 + cosdiff) ** 2)
import math
def computeAngles(x, y):
    x = x* 1.0
    y = y * 1.0
    print("x,y", x, y)
    if(x** 2 + y**2 > 4) :
        normalizingFactor = math.sqrt((3.999)/(x** 2 + y**2))
        print(normalizingFactor)
        x = x * normalizingFactor
        y = y * normalizingFactor

    sumsq = (y ** 2 + x ** 2)
    cosdiff = (sumsq - 2)/2
    sindiff = math.sqrt(1 - cosdiff ** 2)

    numerator = y * (1 + cosdiff) - x * sindiff
    denominator = (0.0001 + sindiff ** 2 + (1 + cosdiff) ** 2)
    sinb = numerator / denominator
    a = math.asin(sinb)
    b = a + math.acos(cosdiff)
    return ((a * 180)/math.pi,((b - a) * 180)/math.pi)
