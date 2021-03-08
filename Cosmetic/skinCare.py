from Cosmetic.SkinType import SkinType
from cosmetic import Cosmetic


class SkinCare(Cosmetic):
    def __init__(self, name, price, producer, category, gender, professional_beauty, field, manufacturing_process,
                 skin_types = SkinType, attributes = "none"):
        super().__init__(name, price, producer, category, gender, professional_beauty, field, manufacturing_process)
        self.skin_types = skin_types
        self.attributes = attributes

    def __repr__(self):
        return (
            f" Name: {self.name} \n Price: {self.price}$ \n Producer: {self.producer} \n Category: {self.category}\n "
            f"Gender types: {self.gender} \n Professional Beauty: {self.professional_beauty}\n"
            f" Field : {self.field}\n Manufacturing Process: {self.manufacturing_process} \n "
            f"Skin Type: {self.skin_types}\n Attributes: {self.attributes}\n ")