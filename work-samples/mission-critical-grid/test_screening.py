import unittest
from screening import screen, transformer_fault_bound

class Qualification(unittest.TestCase):
    def test_capacity(self):
        a=screen()
        self.assertAlmostEqual(a['facility_mw'],31.2)
        self.assertAlmostEqual(a['demand_mva'],32.8421052632)
        self.assertAlmostEqual(a['n_minus_1_loading_pct'],82.1052631579)
        self.assertAlmostEqual(a['normal_loading_pct'],a['n_minus_1_loading_pct']/2)
        self.assertAlmostEqual(screen(it_mw=a['n_minus_1_it_limit_mw'])['n_minus_1_loading_pct'],100)
    def test_fault(self):
        self.assertAlmostEqual(transformer_fault_bound(2.5,.4,.06),60.1406530406)
    def test_invalid(self):
        for fn in (lambda: screen(pf=0),lambda: transformer_fault_bound(2.5,.4,0)):
            with self.assertRaises(ValueError): fn()
