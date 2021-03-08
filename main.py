from lab3.Cosmetic.hairCare import HairCare
from lab3.CosmeticManeger.cosmeticManeger import CosmeticManeger
from lab3.gender import Gender
from lab3.Cosmetic.makeup import Makeup
from lab3.Cosmetic.skinCare import SkinCare
from lab3.CosmeticTools.hairCuttingTools import HairCuttingTools
from lab3.CosmeticTools.makeupBrushes import MakeupBrushes

def main():
    hc = HairCare(name='Nutrisse Nourishing', price=9.76, producer='Garnier', category='Hair Care',
                  gender=Gender.UNISEX.name,
                  professional_beauty=True, field="Medium ", manufacturing_process=False, hair_type='Natural Brown',
                  hair_consern='nourishing', hair_care_attributes='Oil Powered')

    mu = Makeup(name='Rainbow Colors ', price=9.98, producer='BestLand', category='Makeup',
                gender=Gender.FEMALE.name,
                professional_beauty=True, field="Powder", manufacturing_process=False, makeup_format="Palette ",
                makeup_attributes=" Cruelty Free", makeup_for=" Eye")

    sc = SkinCare(name='Aloe Skin Care Cream ', price=89.90, producer='InfiniteAloe', category='Skin Care',
                  gender=Gender.UNISEX.name,
                  professional_beauty=False, field="Jars", manufacturing_process=False, skin_types="All Skin Types",
                  attributes="Original Scent")

    hct = HairCuttingTools(name="Hair Cutting Scissors", price=9.99, producer="Fcysy", category="Hair Cutting Tools",
                           professional_beauty=True, tools_type="Scissors", electric=False, for_lenght_hair=True)

    mb = MakeupBrushes(name="Syntus Makeup Brush Set", price=9.99, producer="Syntus", category="Makeup Brushes",
                       professional_beauty=False, brushes_for="Makeup", lenght_mm="all type", rigidity="hard")

    list_cosmetic = [hc, mu, sc]

    generalManeger = CosmeticManeger(list_cosmetic)

    generalManeger.search_by_gender("FEMALE")
    generalManeger.search_by_category("Hair Cutting Tools")
    generalManeger.sort_by_price(True)
    generalManeger.money_chek(0)

if __name__ == '__main__':
    main()