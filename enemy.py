class Enemy:
    def __init__(self, hp, damage, name, dexterity):
        self.hp = hp
        self.damage = damage
        self.name = name
        self.dexterity = dexterity

    def attack(self, target):
        print(f"{self.name} deals {self.damage} to {target.name}.")
        return target.take_damage(self.damage)
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            # Return 1 for a kill
            return 1
        else:
            return 0
