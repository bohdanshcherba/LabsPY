import unittest
from main import *


class TestCosmeticManeger(unittest.TestCase):

    def setUp(self):
        self.hairCare = HairCare(name='Nutrisse Nourishing', price=9.76, producer='Garnier', category='Hair Care',
                                 gender=Gender.UNISEX.name,
                                 professional_beauty=True, field="Medium ",
                                 manufacturing_process=Types.MachineMade.name,
                                 hair_type='Natural Brown',
                                 hair_consern='nourishing', hair_care_attributes='Oil Powered')
        self.makeup = Makeup(name='Rainbow Colors ', price=9.98, producer='BestLand', category='Makeup',
                             gender=Gender.FEMALE.name,
                             professional_beauty=True, field="Powder", manufacturing_process=Types.HandMade.name,
                             makeup_format="Palette ",
                             makeup_attributes=" Cruelty Free", makeup_for=" Eye")
        self.skinCare = SkinCare(name='Aloe Skin Care Cream ', price=89.90, producer='InfiniteAloe',
                                 category='Skin Care',
                                 gender=Gender.UNISEX.name,
                                 professional_beauty=False, field="Jars", manufacturing_process=Types.MachineMade.name,
                                 skin_types=SkinType.Combination.name,
                                 attributes="Original Scent")
        self.hairCuttingTools = HairCuttingTools(name="Hair Cutting Scissors", price=9.99, producer="Fcysy",
                                                 category="Hair Cutting Tools",
                                                 professional_beauty=True, tools_type="Scissors", electric=False,
                                                 for_lenght_hair=True)
        self.makeupBrushes = MakeupBrushes(name="Syntus Makeup Brush Set", price=20.2, producer="Syntus",
                                           category="Makeup Brushes",
                                           professional_beauty=False, brushes_for="Makeup", lenght_mm="all type",
                                           rigidity="hard")
        list_cosmetic = [self.hairCare, self.makeup, self.skinCare]
        list_all = [self.hairCare, self.makeup, self.skinCare, self.hairCuttingTools, self.makeupBrushes]

        self.cosmetic_maneger = CosmeticManeger(list_cosmetic)
        self.maneger = CosmeticManeger(list_all)

    def test_search_by_gender(self):
        self.assertEqual(self.cosmetic_maneger.search_by_gender("FEMALE"), [self.makeup])

    def test_search_by_category(self):
        self.assertEqual(self.maneger.search_by_category("Hair Cutting Tools"), [self.hairCuttingTools])

    def test_sort_by_price_asc(self):
        self.assertEqual(self.maneger.sort_by_price(SortOrder.ASC),
                         [self.hairCare, self.makeup, self.hairCuttingTools, self.makeupBrushes, self.skinCare])


if __name__ == '__main__':
    unittest.main()
