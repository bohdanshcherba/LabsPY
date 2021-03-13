from items import Items


class CosmeticTools(Items):

    def __init__(self, name, price, producer, category, professional_beauty):
        super().__init__(name, price, producer, category)

        self.professional_beauty = professional_beauty
