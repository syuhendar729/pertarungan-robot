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

    def attack_accuracy(self):
        pass

    def defend(self):
        # Ketika defend diaktifkan, akan mengurangi damage dari attack lawan sebesar defense yang dimiliki
        self.is_defending = True
        print(f"{self.name} bersiap bertahan!")

    def is_alive(self):
        # Mengecek status hidup robot untuk menentukan apakah masih ada next Ronde atau tidak
        return self.hp > 0


class Game():
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play(self):
        # Akan melakukan perulangan Ronde sampai salah satu robot mati
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round} ==========================================================")
            print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack}]")
            print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack}]")

            # Pada aksi ini default nya, Robot1 menyerang terlebih dahulu baru Robot2
            # Jika Robot2 defense, itu dipakai di next Ronde, bukan ronde saat ini
            # Perlu coba dibuat agar 50% kemungkinan siapa duluannya yang memilih aksi
            # Perlu coba dibuat agar defense Robot2 itu tetap jadi defense di Ronde tersebut
            
            # Robot 1 melakukan aksinya terlebih dahulu
            self.player_turn(self.robot1, self.robot2)
            # Jika Robot 2 mati, maka Robot 1 menang
            if not self.robot2.is_alive():
                print(f"{self.robot2.name} menang!")
                break

            
            # Robot 2 melakukan aksinya setelah Robot 1
            self.player_turn(self.robot2, self.robot1)
            # Jika Robot 1 mati, maka Robot 2 menang
            if not self.robot1.is_alive():
                print(f"{self.robot1.name} menang!")
                break
            
            self.round = self.round + 1

    def player_turn(self, player, enemy):
        # Attack: Robot menyerang lawannya
        # Defense: Robot melakukan pertahanan dari attack lawannya, mengurangi damage yg diberikan
        # Regen: Robot melakukan regenerasi yang membuat HP nya naik
        # Giveup: Robot menyerah dari lawan, dan otomatis lawannya menang
        print("\n1. Attack     2. Defense     3. Regen     4. Giveup")
        choice = input(f"{player.name}, pilih aksi: ")
        if choice == '1':
            player.attack_enemy(enemy)
        elif choice == '2':
            player.defend()
        elif choice == '3':
            player.regen_health()
        elif choice == '4':
            print(f"{player.name} menyerah!")
        else:
            print("Pilihan tidak valid!")
            self.player_turn(player, enemy)


# Robot1 => HP: 50, Attack: 20, Defense: 5, Regen: 10
rb1 = Robot("Fufufafa", 50, 20, 5, 10)
# Robot1 => HP: 100, Attack: 10, Defense: 10, Regen: 15
rb2 = Robot("Kukukaka", 100, 10, 10, 15)

game = Game(rb1, rb2)
game.play()


