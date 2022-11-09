import unittest
from A_labb import *


class test_Equilibrium(unittest.TestCase):
    def test_Number(self):#Testar om programmet kan läsa in nummer och inte bara siffor
        self.assertEqual(solve("[[8,5],16]",), 1)


    def test_multiple_strings(self):#Testar om programmet kan läsa in flera stränger i rad
        solve("[[1,2],[3,4]]")
        self.assertEqual(solve("[[1,2],[3,4]]"), 3)

    def test_Solo_Weight(self):#Testar om programmmet kan retunera rätt vid ensamma vikter
        self.assertEqual(solve("1"), 0)

    def test_Empty(self):#testar om det blir error när en tom sträng skickas in
        solve("")

if __name__ == "__main__":
    unittest.main(argv=[""])

#%%

