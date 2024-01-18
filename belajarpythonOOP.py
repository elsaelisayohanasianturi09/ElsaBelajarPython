#Tutorial1

class Food: #Template
    pass
food1 = Food()
food2 = Food()
food3 = Food()

food1.name = "Bakso"
food1.price  = 12000
food1.stock = 30

food2.name = "Mie Ayam"
food2.price = 15000
food2.stock = 39

food3.name = "Soup"
food3.price = 20000
food3.stock = 30

print(food1)
print(food1.name)
print(food2.price)
print(food3.name)


#Tutorial3

print("==================================")
class Food :
    def __init__(self, inputName, inputPrice, inputStock) :
        self.name = inputName
        self.price = inputPrice
        self.stock = inputStock
food1 = Food("Bakso", 12000, 45)
food2 = Food("Mie Ayam", 10000, 13)
food3 = Food("Soup", 15000, 34)

print(food1.__dict__)
print(food2.__dict__)
print(food3.__dict__)

#Tutorial4

print("=====================================")
class Food :
    #Class Variabel
    jumlah = 0

    def __init__(self, inputName, inputPrice, inputStock) :
        self.name = inputName
        self.price = inputPrice
        self.stock = inputStock
        Food.jumlah += 1
        print(f"Membuat Food dengan nama {inputName} " )

food1 = Food("Bakso", 12000, 45)
print(Food.jumlah)
food2 = Food("Mie Ayam", 10000, 13)
print(Food.jumlah)
food3 = Food("Soup", 15000, 34)
print(Food.jumlah)