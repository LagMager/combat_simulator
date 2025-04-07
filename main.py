
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_defending = False

    def deal_damage(self,other):
        other.health -= self.attack
        print(f"{self.name} Attacks {other.name} for {self.attack} Damage!!")
    def defend(self):
        self.is_defending = True
        print(f"{self.name} is defending!")
    def heal(self):
        self.health += 10
        print(f"{self.name} heals 10 HP!")
        
def main():
    #Defining Entities
    player = Character("Player", 100, 20, 5)
    enemy = Character("Enemy", 80, 15, 3)

    player_victory = False
    enemy_victory = False
    player_turn = True
    #Setting up basic loop
    while (player_victory == False) or (enemy_victory == False):
        
        print(f"\nPlayer HP: {player.health}\nEnemy HP: {enemy.health}")
        #Player Turn
        if player_turn == True:
            valid_actions = [1,2,3]
            action = None
            print("\nPlayer Turn")
            print("\nChoose your next action!")
            print("1. Attack\n2. Defend\n3. Heal")
            
            while action not in valid_actions:
                try:
                    action = int(input("> "))
                    if action not in valid_actions:
                        print("Please choose a valid action: 1, 2, or 3.")
                    else:
                        break
                except ValueError:
                    print("Please enter a number (1, 2, or 3).")
        
            match action:
                case 1:
                    player.deal_damage(enemy)
                case 2:
                    player.defend
                case 3:
                    player.heal()

            player_turn = False

            

        #Enemy Turn
        else:
            
            print("I'm evil!")
            print("")
            player_turn = True

    return 0

if __name__ == "__main__":
    main()