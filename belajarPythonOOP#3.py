class Hero :
    jumlahHero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor) :
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

#Method tanpa return
    def siapa(self) :
        print(f"Nama Saya adalah {self.name}")
    def heal(self) :
        print(f"Darah saya sekarang adalah {self.health}")

#Method dengan argumen
    def healthUp(self, up) :
        self.health += up
        print(f"Darah Saya bertambah. Sekarang adalah {self.health}")
        
#Method dengan return
    def getHealth(self) :
        return self.health

hero1 = Hero("Shadow", 100, 10, 5)
hero2 = Hero("Sniper", 200, 3, 9)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.heal()
hero1.healthUp(10)
print(hero1.getHealth())

