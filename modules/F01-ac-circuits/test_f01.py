import math
import unittest
from f01 import solve

class Qualification(unittest.TestCase):
    def test_rlc_reference(self):
        z,i,s=solve(24,50,10,.03,.0001)
        self.assertAlmostEqual(z.real,10)
        self.assertAlmostEqual(z.imag, -22.4062106576, places=8)
        self.assertAlmostEqual(s.real, abs(i)**2*10)
        self.assertLess(s.imag,0)
    def test_pure_resistance(self):
        self.assertEqual(solve(24,50,12,0)[2],48+0j)
    def test_pure_inductance(self):
        self.assertGreater(solve(24,50,0,.03)[2].imag,0)
    def test_pure_capacitance(self):
        self.assertLess(solve(24,50,0,0,.0001)[2].imag,0)
    def test_resonance(self):
        f=1/(2*math.pi*math.sqrt(.03*.0001))
        self.assertAlmostEqual(solve(24,f,10,.03,.0001)[2].imag,0)
    def test_invalid(self):
        with self.assertRaises(ValueError): solve(24,0,10,0)
