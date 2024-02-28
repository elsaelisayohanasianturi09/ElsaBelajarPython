class Hero :
    jumlahHero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor ) :
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlahHero += 1
    def who(self) :
        print(f"Saya adalah Hero : {self.name}")
    def heal(self) :
        print(f"Darah Saya sekarang sebanyak {self.health}")
    def tambahDarah(self, tambah) :
        self.health += tambah
        print(f"Darah Saya bertambah, sekarang darah Saya sebanyak {self.health}")
hero1 = Hero("Shadow", 100, 30, 15)
hero2 = Hero("Sniper", 140, 30, 12)
hero3 = Hero("Wonder Woman", 120, 25, 20)
hero4 = Hero("Spiderman", 180, 10, 25)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)
print()
hero1.who()
hero1.heal()
hero1.tambahDarah(50)
print()
hero2.who()
hero2.heal()
print()
hero3.who()
hero3.heal()
hero3.tambahDarah(20)
print()
hero4.who()
hero4.heal()









