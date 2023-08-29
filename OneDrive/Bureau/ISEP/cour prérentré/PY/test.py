import unittest
from devine_le_prix import verif
class TestJustePrix(unittest.TestCase):
    def test_Bravo(self):
        resultat= verif(5,5)
        self.asserEqual(resultat,0)
    def test_non_trouve(self):
        resultat = verif(5, 3)
        self.asserEqual(resultat,1)
if __name__ =='__main__':
    unittest.main()

