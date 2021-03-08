from lab3.cosmetic import Cosmetic


class HairCare(Cosmetic):
    def __init__(self, name, price, producer, category, gender, professional_beauty, field, manufacturing_process,
                 hair_type, hair_consern, hair_care_attributes):
        super().__init__(name, price, producer, category, gender, professional_beauty, field, manufacturing_process)
        self.hair_type = hair_type
        self.hair_consern = hair_consern
        self.hair_care_attributes = hair_care_attributes


    def __repr__(self):
        return (f" Name: {self.name} \n Price: {self.price}$ \n Producer: {self.producer} \n Category: {self.category}\n "
              f"Gender types: {self.gender} \n Professional Beauty: {self.professional_beauty}\n"
              f" Field : {self.field}\n Manufacturing Process: {self.manufacturing_process} \n "
              f"Hair Type: {self.hair_type}\n Hair Consern: {self.hair_consern}\n Hair Care Attributes: {self.hair_care_attributes} ")


