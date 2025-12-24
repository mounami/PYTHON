import random

class Pokemon:

    def __init__(self, name, attack, hp, defense):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage

        if self.hp < 0:
            self.hp = 0

        return actual_damage
    
    def is_alive(self):
        return self.hp > 0
    
    def attack_opponent(self, opponent):
        """Attack another Pokemon"""
# Random damage: 80-100% of attack stat
        damage = random.randint(int(self.attack * 0.8), self.attack)
        print(f"\n{self.name} attacks {opponent.name}!")

        print(f"\n{self.name} attacks {opponent.name}!")
        actual_damage = opponent.take_damage(damage)
        print(f"{opponent.name} takes {actual_damage} damage!")
        print(f"{opponent.name}'s HP: {opponent.hp}/{opponent.max_hp}")

    def __str__(self):
        """String representation"""
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, ATK: {self.attack}, DEF: {self.defense})"
        
        
# Create Pokemon
pikachu = Pokemon("Pikachu", 100, 25, 10)
charmander = Pokemon("Charmander", 90, 30, 8)

    
# Battle loop
round_num = 1
while pikachu.is_alive() and charmander.is_alive():
    print(f"\n{'='*40}")
    print(f"ROUND {round_num}")
    print(f"{'='*40}")
