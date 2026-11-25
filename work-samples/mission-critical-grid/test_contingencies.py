import unittest
from campus import inputs
from contingencies import inventory,case_network,reachable,index

class TestTopology(unittest.TestCase):
    def setUp(self): self.a=inputs()
    def test_inventory(self): self.assertEqual(len(set(inventory(self.a))),41)
    def test_source_isolation(self):
        n,frac,live=case_network(self.a,('source','A'),'restored')
        self.assertFalse(n.trafo.at[index(n.trafo,'T-HV-A'),'in_service'])
        self.assertTrue(n.switch.closed.iloc[0])
        self.assertNotIn(index(n.bus,'HV-A'),live)
        self.assertEqual(sum(frac),16)
    def test_bus_failure(self):
        n,frac,live=case_network(self.a,('mv_bus','A'),'restored')
        self.assertFalse(n.switch.closed.iloc[0])
        self.assertNotIn(index(n.bus,'MV-A'),live)
        self.assertEqual(sum(frac),16)
    def test_feeder_failure(self):
        n,frac,live=case_network(self.a,('feeder','F01-A'),'initial')
        self.assertEqual(sum(frac),15.5)
        n,frac,live=case_network(self.a,('feeder','F01-A'),'restored')
        self.assertEqual(sum(frac),16)
        self.assertFalse(n.line.at[index(n.line,'F01-A'),'in_service'])
        self.assertEqual(n.load.at[index(n.load,'B01-A-load'),'p_mw'],0)
    def test_coupler_failure(self):
        n,frac,live=case_network(self.a,('coupler','MV coupler'),'restored')
        self.assertFalse(n.switch.closed.iloc[0])
        self.assertEqual(sum(frac),16)
