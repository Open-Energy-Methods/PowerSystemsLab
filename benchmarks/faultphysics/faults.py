"""Synthetic symmetrical-component benchmark; kV, ohm, kA."""
import cmath
import math

A=cmath.exp(2j*math.pi/3)
def to_phase(zero,pos,neg):
    return (zero+pos+neg,zero+A*A*pos+A*neg,zero+A*pos+A*A*neg)

def to_sequence(a,b,c):
    return ((a+b+c)/3,(a+A*b+A*A*c)/3,(a+A*A*b+A*c)/3)

def impedances(c=1.1,sk=500):
    x=c*20**2/sk/math.sqrt(1.01)
    z=complex(.1*x,x)+complex(.5,1.2)
    z0=complex(.4*x,2*x)+complex(1.5,3.6)
    return z,z,z0

def currents(e,z1,z2,z0,zf=0j):
    i3=e/z1
    i1=e/(z1+z2+zf)
    ig=e/(z1+z2+z0+3*zf)
    return {'3ph':to_phase(0,i3,0),'2ph':to_phase(0,i1,-i1),'1ph':to_phase(ig,ig,ig)}

def reference(c=1.1,sk=500):
    z1,z2,z0=impedances(c,sk)
    return {k:max(map(abs,v)) for k,v in currents(c*20/math.sqrt(3),z1,z2,z0).items()}

def parallel_paths(c=1.1,sk=500):
    # Independent identical sources, equal phase, no shared upstream impedance.
    # Illustrative equal branches, not campus coupler operation.
    z1,_,_=impedances(c,sk)
    e=c*20/math.sqrt(3)
    return {'open_ka':abs(e/z1),'closed_ka':abs(e/(z1/2))}
