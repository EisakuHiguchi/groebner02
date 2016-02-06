import re
from sympy import *

x, y, z = symbols('x y z')

def getdxdt():
    return (z - 0.7)*x - 3.5*y

def getdydt():
    return 3.5*x + (z - 0.7)*y

def getdzdt(a):
    return a + z + (z**3)/3 - (x**2 + y**2)*(1 + 0.25*z)


def getGroebner(x0, y0, z0, dt, a):
    dx = getdxdt() - x0/dt
    dy = getdydt() - y0/dt
    dz = getdzdt(a) - z0/dt

    return groebner([dx,dy,dz])

def solveGb(gb):
    res = []
    gb.exprs.reverse()
    for e in gb.exprs:
        res.append(solve(Eq(e,0)))
    return res