import unittest
from reference import load_flow, fault
class ReferenceTests(unittest.TestCase):
    def test_voltage(self):
        a=load_flow(); self.assertAlmostEqual(a['vm_pu'],0.9950630645714081); self.assertAlmostEqual(a['va_degree'],-0.2879014540033181)
    def test_balance(self):
        a=load_flow(); self.assertAlmostEqual(a['p_source_mw']-a['p_loss_mw'],2); self.assertAlmostEqual(a['q_source_mvar']-a['q_loss_mvar'],.8)
    def test_fault(self):
        self.assertAlmostEqual(fault(1.1,500),5.888071061601967); self.assertAlmostEqual(fault(1,250),4.0249966728095785)
if __name__=='__main__': unittest.main()
