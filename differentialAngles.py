# calculate the angles based on the differential
# x = l cos(a) + l cos(b)
# y = l sin(a) + l sin(b)
# differentiate for da and db
import math

def calcAngles(x,y,a,b):
    x0 = math.cos(a) + math.cos(b)
    y0 = math.sin(a) + math.sin(b)
    dx = (x-x0)
    dy = (y-y0)
    ares = a
    bres = b
    minl = dx * dx + dy * dy
    for iteration in range(1,500) :
        x0 = math.cos(a) + math.cos(b)
        y0 = math.sin(a) + math.sin(b)
        dx = (x-x0)
        dy = (y-y0)
        if(dx * dx + dy * dy < minl) :
            ares = a
            bres = b
        sinba = math.sin(b - a)
        if(sinba == 0) : sinba = 0.01
        da = 1.00000 * (dy * math.sin(b) + dx * math.cos(b))/sinba
        db = -1.00000 * (dy * math.sin(a) + dx * math.cos(a))/sinba
        modsum = 0.0001 + abs(da) + abs(db)
        da = da/modsum
        db = db/modsum
        a = a + 0.01 * da
        b = b + 0.01 * db
    return (ares,bres)