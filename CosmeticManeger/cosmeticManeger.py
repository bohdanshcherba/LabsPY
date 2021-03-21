from CosmeticManeger.sortOrder import SortOrder
from operator import attrgetter
from gender import Gender


class CosmeticManeger():
    def __init__(self, items=list):
        self.items = list(items)

    # def search_by_gender(self, gender=Gender):
    #     for i in self.items:
    #         if i.gender == gender:
    #
    #             print(i)
    #             print("----------------------------------------------")

    def search_by_gender(self, gender=Gender):
        out = list()
        for i in self.items:
            if i.gender == gender:
                out.append(i)
        self.items = out
        return out


    def search_by_category(self, category):
        for i in self.items:
            if i.category == category:
                print(i)
                print("----------------------------------------------")

    def sort_by_price(self, type = SortOrder):
        sort = sorted(self.items, key=attrgetter('price'), reverse=type)
        for i in sort:
            print(i)
            print("___________________________________________")

    def money_chek(self, money):
        if money > 0:
            for i in self.items:
                if i.price <= money:
                    print(i)
        else:
            print("no goods for you :(")

    def print_items(self):
        for item in self.items:
            print(type(item))
            print(str(item))