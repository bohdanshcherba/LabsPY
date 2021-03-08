from cosmetic import Cosmetic


class Makeup(Cosmetic):
    def __init__(self, name, price, producer, category, gender, professional_beauty,
                 field, manufacturing_process, makeup_format, makeup_attributes, makeup_for):
        super().__init__(name, price, producer, category, gender, professional_beauty, field, manufacturing_process)
        self.makeup_format = makeup_format
        self.makeup_attributes = makeup_attributes
        self.makeup_for = makeup_for

    def __repr__(self):
        return (
            f" Name: {self.name} \n Price: {self.price}$ \n Producer: {self.producer} \n Category: {self.category}\n "
            f"Gender types: {self.gender} \n Professional Beauty: {self.professional_beauty}\n"
            f" Field : {self.field}\n Manufacturing Process: {self.manufacturing_process} \n "
            f"Makeup Format: {self.makeup_format}\n Makeup Attributes: {self.makeup_attributes}\n Makeup For: {self.makeup_for} ")