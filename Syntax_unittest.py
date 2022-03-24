import unittest

from Syntax import *

class SyntaxTest(unittest.TestCase):
    def testCorrectMolecule(self):#testar rätt molekyl
        with open("korrekt_indata.txt","r",encoding="utf-8") as file:
            for line in file:
                self.assertEqual(test_molecule(line), "Formeln är syntaktiskt korrekt" )

    def testWrongMolecule(self):#testar fel molekyl
        with open ("Felaktig_indata.txt","r",encoding="utf-8") as file1, open("Felaktig_utdata.txt","r",encoding="utf-8") as file2:
            for line1, line2 in zip(file1, file2):
                self.assertEqual(test_molecule(line1).strip(), line2.strip())#tittar om fel indata ger rätt utdata


if __name__ == "__main__":
    unittest.main(argv=[""]) #behövs när programet körs i dataspell


#%%
