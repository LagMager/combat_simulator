class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_defending = False

    def deal_damage(self,other):
        if other.is_defending == True:
            other.health -= (self.attack - other.defense)
        else:
            other.health -= self.attack
        print(f"\n{self.name} Attacks {other.name} for {self.attack} Damage!!")
    def defend(self):
        self.is_defending = True

        print(f"\n{self.name} shields themselves!")
    def heal(self):
        self.health += 10
        print(f"\n{self.name} heals 10 HP!")