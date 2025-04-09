
import random


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
            player_action = None
            print("\nPlayer Turn")
            print("\nChoose your next action!")
            print("1. Attack\n2. Defend\n3. Heal")
            
            while player_action not in valid_actions:
                try:
                    player_action = int(input("> "))
                    if player_action not in valid_actions:
                        print("Please choose a valid action: 1, 2, or 3.")
                    else:
                        break
                except ValueError:
                    print("Please enter a number (1, 2, or 3).")
        
            match player_action:
                case 1:
                    player.deal_damage(enemy)
                case 2:
                    player.defend
                case 3:
                    player.heal()

            player_turn = False

            

        #Enemy Turn
        else:
            enemy_action = random.randrange(1,3)
            print(enemy_action)
            match enemy_action:
                case 1:
                    enemy.deal_damage(player)
                case 2:
                    enemy.defend
                case 3:
                    enemy.heal()
            player_turn = True

        #Win Check

        if player.health == 0:
            enemy_victory = True
        elif enemy.health == 0:
            player_victory = True
        

    return 0

if __name__ == "__main__":
    main()