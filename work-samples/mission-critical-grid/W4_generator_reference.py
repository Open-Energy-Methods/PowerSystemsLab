"""Illustrative fixed-field comparison, not an actual equipment duty model."""
import math

def fixed_field(t):
    xd,xtr,xsub=2.36,.16,.12
    return 1/xd+(1/xtr-1/xd)*math.exp(-t/.164)+(1/xsub-1/xtr)*math.exp(-t/.008)

def main():
    ibase=2.5/(math.sqrt(3)*.4)
    print(f'base={ibase:.9f} kA')
    print(f'initial={ibase*fixed_field(0):.9f} kA')
    print(f'fixed-field asymptote={ibase/2.36:.9f} kA')
    print('published separately excited sustained=11.142 kA')
    for t in (0,.01,.05,.1,.2,.5,1):
        print(f'{t:.3f} s: {ibase*fixed_field(t):.9f} kA')
if __name__=='__main__': main()
