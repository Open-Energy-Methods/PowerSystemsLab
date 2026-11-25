"""Educational RMS-envelope inverse-time relay; not a vendor relay."""
import math

def rate(current,pickup,tms):
    if not all(math.isfinite(x) for x in (current,pickup,tms)) or current<0 or pickup<=0 or tms<=0:
        raise ValueError('invalid relay input')
    m=current/pickup
    return math.expm1(.02*math.log(m))/(.14*tms) if m>1 else 0.

def time_constant(current,pickup,tms):
    r=rate(current,pickup,tms)
    return 1/r if r else math.inf

def integrate(samples,pickup,tms):
    """Piecewise constant RMS magnitudes, positive durations; instantaneous reset below/equal pickup."""
    t=progress=peak=0.
    for current,dt in samples:
        if not math.isfinite(dt) or dt<=0: raise ValueError('invalid duration')
        r=rate(current,pickup,tms)
        if r:
            new=progress+r*dt
            if new>=1:
                return {'trip_s':t+(1-progress)/r,'peak_progress':1.}
            progress=new
        else:
            progress=0.
        peak=max(peak,progress)
        t+=dt
    return {'trip_s':None,'peak_progress':peak}

def envelope(t):
    # Assumed generic amplitudes and short-circuit time constants; not OEM data.
    return 1.25+3.4*math.exp(-t/.04)+3.35*math.exp(-t/.2)

def decay_case(pickup=2,tms=.1,dt=.0001):
    n=round(2/dt)
    return integrate(((envelope((k+.5)*dt),dt) for k in range(n)),pickup,tms)
