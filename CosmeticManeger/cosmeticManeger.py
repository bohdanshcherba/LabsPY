from CosmeticManeger.sortOrder import SortOrder
from operator import attrgetter
from gender import Gender

# class Test:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def __repr__(self):
#         return f'{self.name}{self.gender}'

class CosmeticManeger():
    def __init__(self, items=list):
        self.items = list(items)

    def search_by_gender(self, gender = Gender):
        for i in self.items:
            if i.gender == gender:
                print(i)
                print("----------------------------------------------")


    def search_by_category(self,category):
        for i in self.items:
            if i.category == category:
                print(i)
                print("----------------------------------------------")

    def sort_by_price(self, SortOrder = SortOrder):
        sortedd = sorted(self.items, key=attrgetter('price'), reverse=True)
        for i in sortedd:
            print(i)
            print("___________________________________________")



    def money_chek(self, money):
        if money > 0:
            for i in self.items:
                if i.price <= money:
                    print(i)
        else:
            print("no goods for you :(")
# if __name__ == '__main__':
#     test = Test("Some Name" , Gender.UNISEX.name)
#     test2 = Test("Some Name2" , Gender.FEMALE.name)
#     test3 = Test("Some Name3" , Gender.UNISEX.name)
#
#     Test_list = [test, test2, test3]
#
#     me = CosmeticManeger(Test_list)
#
#     me.search_by_gender("FEMALE")


