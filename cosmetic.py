from lab3.items import Items


class Cosmetic(Items):
    def __init__(self, name, price, producer, category, gender, professional_beauty, field, manufacturing_process):
        super().__init__(name, price, producer, category)
        self.gender = gender
        self.professional_beauty = professional_beauty
        self.field = field
        self.manufacturing_process = manufacturing_process