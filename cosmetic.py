from items import Items
from Cosmetic.types import Types


class Cosmetic(Items):
    def __init__(self, name, price, producer, category, gender, professional_beauty, field, manufacturing_process = Types):
        super().__init__(name, price, producer, category)
        self.gender = gender
        self.professional_beauty = professional_beauty
        self.field = field
        self.manufacturing_process = manufacturing_process