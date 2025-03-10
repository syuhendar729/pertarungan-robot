from robot import Robot

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
                print(f"{self.robot1.name} menang!")
                break

            
            # Robot 2 melakukan aksinya setelah Robot 1
            self.player_turn(self.robot2, self.robot1)
            # Jika Robot 1 mati, maka Robot 2 menang
            if not self.robot1.is_alive():
                print(f"{self.robot2.name} menang!")
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
            enemy.hp = 0
        else:
            print("Pilihan tidak valid!")
            self.player_turn(player, enemy)


# Robot1 => HP: 50, Attack: 20, Defense: 5, Regen: 10
rb1 = Robot("Fufufafa", 50, 20, 5, 10)
# Robot1 => HP: 100, Attack: 10, Defense: 10, Regen: 15
rb2 = Robot("Kukukaka", 100, 10, 10, 15)

game = Game(rb1, rb2)
game.play()


