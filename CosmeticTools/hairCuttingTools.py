from lab3.cosmeticTools import CosmeticTools


class HairCuttingTools(CosmeticTools):
    def __init__(self, name, price, producer, category, professional_beauty, tools_type, electric, for_lenght_hair):
        super().__init__(self, name, price, producer, category, professional_beauty)
        self.tools_type = tools_type
        self.electric = electric
        self.for_lenght_hair = for_lenght_hair
    def __repr__(self):
        return (
            f"Name: {self.name} \n Price: {self.price}$ \n Producer: {self.producer} \n Category: {self.category}\n "
            f" \n Professional Beauty: {self.professional_beauty}\n "
            f"Tools type: {self.tools_type}\n Electric type: {self.electric} \n For lenght hair: {self.for_lenght_hair}")