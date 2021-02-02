# calculate the angles based on the differential
# x = l cos(a) + l cos(b)
# y = l sin(a) + l sin(b)
import math

def calcAngles(x,y,a,b):
    for iteration in range(1,500) :
        x0 = math.cos(a) + math.cos(b)
        y0 = math.sin(a) + math.sin(b)
        dx = (x-x0)
        dy = (y-y0)
        sina = math.sin(a)
        if(sina == 0) : sina = 0.0001
        sinb = math.sin(b)
        if(sinb == 0) : sinb = 0.0001
        cosa = math.cos(a)
        if(cosa == 0) : cosa = 0.0001
        cosb = math.cos(b)
        if(cosb == 0) : cosb = 0.0001
        dax = (-1.000 * (dx))/(sina)
        dbx = (-1.000 * (dx))/(sinb)
        day = (1.000 * dx)/(cosa)
        dby = (1.000 * dy)/(cosb)
        print(x0, y0, a,b, dax, day, dbx,dby)
        a = a + 0.0001 * dax + 0.0001 * day
        b = b + 0.0001 * dbx + 0.0001 * dby
    return (a,b)