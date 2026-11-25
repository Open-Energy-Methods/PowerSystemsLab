"""Independent balanced two-bus reference, using kV/MW/Mvar/ohm/kA."""
import math
import cmath

V = 20.0
P = 2.0
Q = 0.8
Z = complex(0.5, 1.2)

def load_flow():
    a = 2*(Z.real*P + Z.imag*Q)-V**2
    b = abs(Z)**2*(P**2+Q**2)
    w = (-a+math.sqrt(a*a-4*b))/2
    vr = complex((w+Z.real*P+Z.imag*Q)/V,(Z.real*Q-Z.imag*P)/V)
    current = (V-vr)/Z
    source = V*current.conjugate()
    return dict(vm_pu=abs(vr)/V, va_degree=math.degrees(cmath.phase(vr)), p_source_mw=source.real, q_source_mvar=source.imag, p_loss_mw=(abs(current)**2*Z).real, q_loss_mvar=(abs(current)**2*Z).imag)

def fault(c, sk_mva):
    x=c*V**2/sk_mva/math.sqrt(1+0.1**2)
    return c*V/(math.sqrt(3)*abs(complex(.1*x,x)+Z))

if __name__ == '__main__':
    print(load_flow())
    print('fault max/min kA',fault(1.1,500),fault(1.0,250))
