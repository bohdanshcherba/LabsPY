import unittest

from CosmeticManeger.cosmeticManeger import CosmeticManeger
from Cosmetic import *
from CosmeticTools import *

from main import *

class TestCosmeticManeger(unittest.TestCase):

    def setUp(self) :
        #self.hairCare = HairCare()
        self.makeup = Makeup()
        #self.skinCare = SkinCare()
        #self.hairCuttingTools = HairCuttingTools()
        #self.makeupBrushes = MakeupBrushes()
        #list_cosmetic = [self.hairCare, self.makeup, self.skinCare]
        #list_all = [self.hairCare, self.makeup, self.skinCare, self.hairCuttingTools, self.makeupBrushes]
        list_cosmetic = [self.makeup]
        self.cosmetic_maneger = CosmeticManeger(list_cosmetic)
       # self.maneger = CosmeticManeger(list_all)


    def test_search_by_gender(self):
        self.assertEqual(self.cosmetic_maneger.search_by_gender("FEMALE"), [self.makeup])


if __name__ == '__main__':
    unittest.main()
