class Pos:
    def __init__(self, store, sale):
        self.store = store
        self.__sale = sale  # sale property is private, we cant access

    def get_sale(self):
        return self.__sale

    def set_sale(self, sale):
        if sale >= 0:
            self.__sale = sale
        else:
            print("Sale cannot be negative")


p1 = Pos("shell", 13000)

print(p1.get_sale())

p1.set_sale(8888)
print(p1.get_sale())
