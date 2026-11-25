import unittest
import math
from faults import currents,impedances,reference,to_phase,to_sequence,parallel_paths
from relay import time_constant,integrate,decay_case

class FaultTests(unittest.TestCase):
    def test_roundtrip(self):
        a=(1+2j,3-4j,5+6j)
        for x,y in zip(a,to_phase(*to_sequence(*a))): self.assertAlmostEqual(abs(x-y),0)
    def test_boundary_conditions(self):
        r=currents(1,1j,1j,3j)
        self.assertAlmostEqual(abs(sum(r['3ph'])),0)
        self.assertAlmostEqual(abs(r['2ph'][0]),0)
        self.assertAlmostEqual(abs(r['2ph'][1]+r['2ph'][2]),0)
        self.assertAlmostEqual(abs(r['1ph'][1])+abs(r['1ph'][2]),0)
    def test_reference(self):
        r=reference()
        for k,v in {'3ph':5.888071061601967,'2ph':5.099219118635311,'1ph':3.8210145976348233}.items(): self.assertAlmostEqual(r[k],v)
    def test_equal_sequence(self):
        r=currents(1,1j,1j,1j)
        self.assertAlmostEqual(abs(r['3ph'][0]),abs(r['1ph'][0]))
    def test_parallel(self):
        r=parallel_paths();self.assertAlmostEqual(r['closed_ka'],2*r['open_ka'])

class RelayTests(unittest.TestCase):
    def test_constant(self):
        expected=.14*.1/(5**.02-1)
        self.assertAlmostEqual(time_constant(5,1,.1),expected)
        self.assertAlmostEqual(integrate([(5,.01)]*100,1,.1)['trip_s'],expected)
    def test_piecewise(self):
        t1=time_constant(4,1,.1)
        t2=time_constant(6,1,.1)
        r=integrate([(4,t1*.4),(6,t2)],1,.1)
        self.assertAlmostEqual(r['trip_s'],t1*.4+t2*.6)
    def test_reset(self):
        t=time_constant(5,1,.1)
        self.assertIsNone(integrate([(5,.6*t),(.9,.1),(5,.6*t)],1,.1)['trip_s'])
    def test_below_pickup(self):
        self.assertTrue(math.isinf(time_constant(1,1,.1)))
        self.assertIsNone(integrate([(1,10)],1,.1)['trip_s'])
    def test_decay_convergence(self):
        a=decay_case(dt=.001);b=decay_case(dt=.0001)
        self.assertIsNone(a['trip_s']);self.assertIsNone(b['trip_s'])
        self.assertLess(abs(a['peak_progress']-b['peak_progress']),.001)
    def test_invalid(self):
        with self.assertRaises(ValueError): integrate([(4,-1)],1,.1)
