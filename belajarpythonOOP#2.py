# OOP punya 4 pilar/prinsip/ :
# 1. Encapsulation : menyembunyikan informasi
# 2. Inheritance : ppewarisan / turunan kelas
# 3. Polymorphism : banyak bentuk
# 4. Abstraction : menyembunyikan detail

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass


# encapsulation
"""class Human:
    def _init_(self, name, paslon : int):
        self.name = name
        self.__paslon = paslon

elsa = Human("Elsa", 2)"""

#---------------------------------------------

class Food :
    def __init__(self, inputName : str,  inputHeal : int):
        self.name = inputName
        self.heal = inputHeal
        

class Animal :
    def __init__(self, inputName : str, inputColour : str , inputBlood : int):
        self.name = inputName
        self.colour = inputColour
        self.blood = inputBlood

    def showBlood(self):
        print(f"{self.name} darahnya sekarang {self.blood}")
    def hit(self, target):
        print(f"{self.name}  memukul {target.name}! darah berkurang 10")
        target.blood -= 10
    def sleep(self):
        print(f"{self.name} tidur") 
    def eat(self, food : Food):
        print(f"{self.name} makan {food.name}! darah bertambah {food.heal}")
        self.blood += food.heal
        

food1 = Food("Bayam", 40)
food2 = Food("Wortel", 60)
food3 = Food("Cabai", 20)

animal1 = Animal("Kucing", "White", 190)
animal2 = Animal("Anjing", "Black", 180)
animal3 = Animal("Kelinci", "Yellow", 170)

animal2.showBlood()

animal1.hit(animal2)
animal2.showBlood()

animal1.hit(animal2)
animal2.showBlood()

animal1.hit(animal2)
animal2.showBlood()

animal2.eat(food1)
animal2.showBlood()