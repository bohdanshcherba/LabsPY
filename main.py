from Cosmetic.hairCare import HairCare
from CosmeticManeger.cosmeticManeger import CosmeticManeger
from gender import Gender
from Cosmetic.makeup import Makeup
from Cosmetic.skinCare import SkinCare
from CosmeticTools.hairCuttingTools import HairCuttingTools
from CosmeticTools.makeupBrushes import MakeupBrushes
from Cosmetic.types import Types
from Cosmetic.SkinType import SkinType

customer_money = 0



def main():
    hc = HairCare(name='Nutrisse Nourishing', price=9.76, producer='Garnier', category='Hair Care',
                  gender=Gender.UNISEX.name,
                  professional_beauty=True, field="Medium ", manufacturing_process=Types.MachineMade.name,
                  hair_type='Natural Brown',
                  hair_consern='nourishing', hair_care_attributes='Oil Powered')

    mu = Makeup(name='Rainbow Colors ', price=9.98, producer='BestLand', category='Makeup',
                gender=Gender.FEMALE.name,
                professional_beauty=True, field="Powder", manufacturing_process=Types.HandMade.name,
                makeup_format="Palette ",
                makeup_attributes=" Cruelty Free", makeup_for=" Eye")

    sc = SkinCare(name='Aloe Skin Care Cream ', price=89.90, producer='InfiniteAloe', category='Skin Care',
                  gender=Gender.UNISEX.name,
                  professional_beauty=False, field="Jars", manufacturing_process=Types.MachineMade.name,
                  skin_types=SkinType.Combination.name,
                  attributes="Original Scent")

    hct = HairCuttingTools(name="Hair Cutting Scissors", price=9.99, producer="Fcysy", category="Hair Cutting Tools",
                           professional_beauty=True, tools_type="Scissors", electric=False, for_lenght_hair=True)

    mb = MakeupBrushes(name="Syntus Makeup Brush Set", price=20.2, producer="Syntus", category="Makeup Brushes",
                       professional_beauty=False, brushes_for="Makeup", lenght_mm="all type", rigidity="hard")


    list_cosmetic = [hc , mu , sc]
    list_all = [hc , mu , sc,mb,hct]
    list_tools = [mb,hct]

    generalManeger = CosmeticManeger(list_all)
    cosmeticManeger = CosmeticManeger(list_cosmetic)
    cosmeticManeger.search_by_gender("FEMALE")
    cosmeticManeger.search_by_category("Hair Cutting Tools")
    generalManeger.sort_by_price(SortOrder=True)
    generalManeger.money_chek(customer_money)


if __name__ == '__main__':
    main()
