import random

class Robot():
    def __init__(self, name, hp, attack, defense, regen):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.regen = regen
        self.is_defending = False

    def attack_enemy(self, enemy):
        # Mencoba menyerang lawan dengan kemungkinan berhasilnya adalah 80%
        if random.random() < 0.8:
            damage = self.attack - (enemy.defense if enemy.is_defending else 0)
            damage = max(damage, 0)
            enemy.hp = enemy.hp - damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan damage sebesar {damage}!")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!")
        # Mereset defend lawan menjadi False agar bisa diserang di next Ronde
        enemy.is_defending = False

    def regen_health(self):
        # Mengembalikan HP sesuai regen yg dimiki Robot tersebut
        self.hp = self.hp + self.regen
        print(f"{self.name} meregen HP sebanyak {self.regen} menjadi {self.hp}!")

    def attack_accuracy(self):
        pass

    def defend(self):
        # Ketika defend diaktifkan, akan mengurangi damage dari attack lawan sebesar defense yang dimiliki
        self.is_defending = True
        print(f"{self.name} bersiap bertahan!")

    def is_alive(self):
        # Mengecek status hidup robot untuk menentukan apakah masih ada next Ronde atau tidak
        return self.hp > 0
