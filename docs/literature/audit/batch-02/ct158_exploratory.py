"""Reconstruct CT158 simplified diagrams; exploratory verification, not design."""
import math
import numpy as np

def reactance(closed, zero):
    ybus=np.zeros((4,4),complex)
    def add(i,j,x):
        y=1/(1j*x)
        ybus[i,i]+=y
        if j is not None:
            ybus[j,j]+=y
            ybus[i,j]-=y
            ybus[j,i]-=y
    if zero:
        add(0,None,2.7)
        add(0,1,15.75);add(0,2,42);add(1,3,21)
        if closed:add(2,3,31.5)
    else:
        add(0,None,5.8);add(0,None,99)
        add(1,None,288);add(2,None,288)
        add(0,1,5.25);add(0,2,14);add(1,3,7)
        if closed:add(2,3,10.5)
    return float(np.linalg.solve(ybus,[0,0,0,1])[3].imag)

def currents(x1,x0,c):
    return c*30/(math.sqrt(3)*x1),c*30*math.sqrt(3)/(2*x1+x0)

if __name__=='__main__':
    for closed,expected in [(False,(17.25,39.45,1.104,.773)),(True,(13.05,27.2,1.460,1.072))]:
        x1,x0=reactance(closed,False),reactance(closed,True)
        actual=(x1,x0,*currents(x1,x0,1.1))
        assert all(abs(a-b)/b<.01 for a,b in zip(actual,expected))
        print(closed,actual,currents(x1,x0,1.0))
