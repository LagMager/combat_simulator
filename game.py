"""
game.py
========

This module implements the main game loop for the Combat Simulator, a text-based game where players fight enemies in turn-based combat.

Classes:
--------
- None (relies on the `Character` class from `character.py`).

Functions:
----------
- main():
    The main function that initializes the game, sets up the player and enemy, and runs the game loop.

Game Flow:
----------
1. The player and enemy are initialized as instances of the `Character` class.
2. The game alternates between the player's turn and the enemy's turn.
3. On the player's turn, they can choose to:
    - Attack: Deal damage to the enemy.
    - Defend: Reduce incoming damage on the next enemy attack.
    - Heal: Restore some health.
4. On the enemy's turn, a random action is chosen (attack, defend, or heal).
5. The game ends when either the player's or the enemy's health reaches 0.

Dependencies:
-------------
- `random`: Used to determine the enemy's actions.
- `character.Character`: The class that defines the player and enemy entities.

Usage:
------
Run the script directly to start the game:
    $ python game.py
"""

import random
from character import Character
        
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