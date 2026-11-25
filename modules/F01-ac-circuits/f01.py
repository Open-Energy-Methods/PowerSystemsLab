"""AI-assisted reference solution; learner competence not assessed."""
import math

def solve(v, f, r, l, c=None):
    if not all(math.isfinite(x) for x in (v,f,r,l)) or v < 0 or f <= 0 or r < 0 or l < 0:
        raise ValueError('invalid inputs')
    if c is not None and (not math.isfinite(c) or c <= 0):
        raise ValueError('invalid capacitance')
    w = 2*math.pi*f
    z = complex(r, w*l - (0 if c is None else 1/(w*c)))
    if abs(z) < 1e-12:
        raise ValueError('ideal zero impedance')
    i = v/z
    s = v*i.conjugate()
    return z, i, s

if __name__ == '__main__':
    z,i,s=solve(24,50,10,.03,.0001)
    print(f'Z={z:.9f} ohm; I={i:.9f} A; P={s.real:.9f} W; Q={s.imag:.9f} var; |S|={abs(s):.9f} VA')
