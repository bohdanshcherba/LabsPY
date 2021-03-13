from cosmeticTools import CosmeticTools


class MakeupBrushes(CosmeticTools):
    def __init__(self, name, price, producer, category, professional_beauty, brushes_for, lenght_mm,
                 rigidity):
        super().__init__(name, price, producer, category, professional_beauty)
        self.brushes_for = brushes_for
        self.lenght_mm = lenght_mm
        self.rigidity = rigidity
    def __repr__(self):
        return (f"Name: {self.name} \n Price: {self.price}$ \n Producer: {self.producer} \n Category: {self.category}\n "
            f" \n Professional Beauty: {self.professional_beauty}\n "
            f"brushes for: {self.brushes_for}\n lenght_mm type: {self.lenght_mm} \n rigidity: {self.rigidity}")
