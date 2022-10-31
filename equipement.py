from email.mime import base


class Equipment:
    def __init__(self, armor_rating, slot, name, desc):
        # armor rating given to the wearer
        self.armor_rating = armor_rating
        # what armor slot armor is equipped to
        self.slot = slot
        self.name = name
        self.desc = desc


class Weapon:
    def __init__(self, base_damage, hand, name, desc) -> None:
        self.base_damage = base_damage
        self.hand = hand
        self.name = name
        self.desc = desc
