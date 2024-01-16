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

print("==================================")
class Food :
    def __init__(self, inputName, inputPrice) :
        self.name = inputName
        self.price = inputPrice

food1 = Food("Mie Ayam")
food1 = Food(12000)

food2 = Food("Bakso")
food2 = Food(40000)

food3 = Food("Soup")
food3 = Food(60000)

print(food1.name)
print(food1.price)
print(food2.name)
print(food2.price)
print(food3.name)
print(food3.price)
