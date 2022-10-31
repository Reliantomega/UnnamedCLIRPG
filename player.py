from math import *
from unittest import case
from skill import *
from skill_list import *
from room import *
from room_list import *


# Guess ill just make a CLI 
class Player:
    def __init__(self, name, room, race, origin, gender, trait, stats):
        # get some basic stuff
        self.name = name
        self.race = race
        self.origin = origin
        self.gender = gender
        self.trait = trait
        self.job = ""
        self.level = 1
        self.xp = 0
        self.free_stat_points = 0
        self.current_room: Room = room

        # Affects amount of MP the player has
        self.magic = stats[0]
        # Affects Physical Attack strength and minor effect on sp and very minor effect on HP
        self.strength = stats[1]
        # Affects health and stamina
        self.vitality = stats[2]
        # Reduces amount of damage taken
        self.armor = 0
        # Directly affects magic attack, and has a minor impact on MP
        self.will = stats[3]
        # Affects the amount SP and dodge chance.
        self.dexterity = stats[4]
        # Players will be able to receive blessings and other modifiers from gear and other sources, resulting in a
        # percentage gain in resources
        self.mp_modifier = 0
        self.hp_modifier = 0
        self.sp_modifier = 0

        # Equipment
        self.r_hand = None
        self.l_hand = None
        self.hands = None
        self.head = None
        self.chest = None
        self.legs = None
        self.feet = None

        # Calculate initial Parameters
        self.max_hp = floor(floor(((self.vitality * 10) + floor((self.strength * .25))) * (1 + self.hp_modifier)))
        self.max_mp = floor(floor((self.magic * 5) + floor(self.will * .25)) * (1 + self.mp_modifier))
        self.max_sp = floor(
            floor((self.vitality * 2) + floor(self.dexterity * 5) + (self.strength * .5)) * (1 + self.sp_modifier))
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.sp = self.max_sp

        # Skills and stuff will come later, but i will make a variable for it now
        self.skills = {"meditate": skills["Meditate"]}
        self.spells = []
        self.attacks = []
        self.blessings = []
        self.curses = []
        self.effects = []

    def recalculate_params(self):
        self.max_hp = floor(((self.vitality * 10) + floor((self.strength * .25))) * (1 + self.hp_modifier))
        self.max_mp = floor((self.magic * 5) + floor(self.will * .25) * (1 + self.mp_modifier))
        self.max_sp = floor((self.vitality * 10) + floor(self.strength * .5) * (1 + self.sp_modifier))

    def full_heal(self):
        self.hp, self.mp, self.sp = self.max_hp, self.max_mp, self.max_sp

    def assign_job(self, job):
        # change some stats based on the job assigned and what not, only initial assignment
        if job == "warrior":
            self.job="warrior"
            self.vitality += 15
            self.strength += 10
            self.recalculate_params()
            return

        if job == "mage":
            self.job = "mage"
            self.magic += 15
            self.will += 10
            self.recalculate_params()
            return

    def print_params(self):
        print(f"HP:{self.hp}\nMP:{self.mp}\nSP:{self.sp}\n")

    def learn_spell(self, spell):
        self.spells.append(spell)

    def learn_skill(self, skill):
        self.skills.append(skill)

    def meditate(self):
        if self.mp < self.max_mp:
            self.mp += 10 * self.skills[0].level
        if self.mp > self.max_mp:
            self.mp = self.max_mp

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            # Return 1 for a kill
            return 1
        else:
            return 0

    def attack(self, target, damage):
        print(f"You deal {damage} to {target.name}.")
        return target.take_damage(damage)

    def cast(self, target, spell: int):
        # TODO: change this calculation
        if self.mp < self.spells[spell].cost:
            print("Not enough mana")
            return 0
        self.mp -= self.spells[spell].cost
        return self.attack(target, floor(self.spells[spell].damage * ((100 + self.will) / 100)))

    def examine_room(self):
        print(self.current_room.desc)

    def level_up(self):
        # Leveling up increases stats across the board, according to the job. at the the beginning, the stats are
        # distributed evenly. every other level you get 3 addition stat points to distribute.
        self.level += 1
        for job in self.jobs:
            if job == "mage":
                self.will += 2
                self.magic += 2
                self.vitality += 1
            elif job == "warrior":
                self.strength += 2
                self.vitality += 2
                self.dexterity += 1
            elif job == "none":
                self.strength += 1
                self.vitality += 1
                self.dexterity += 1
                self.magic += 1
                self.will += 1
        if self.level % 2 == 0:
            self.free_stat_points += 3
            u_in = input(
                f"You have {self.free_stat_points} stat points to distribute. Would you like to spend them now? You "
                f"will not be able to spend them again until you level up. Y/n\n>")
            if u_in.lower() == "y":
                while self.free_stat_points > 0:
                    # TODO: Add input Verification
                    stat_in = input(
                        "What stat would you like to improve? (S)trength, (V)itality, (M)agic, (W)ill, (D)exterity?\n>")
                    amount_in = int(input(
                        f"How many points would you like to allocate? You have {self.free_stat_points} remaining.\n>"))
                    confirm = input(f"Are you sure you would like to allocate {amount_in} to {stat_in}? Y/n\n>")
                    if confirm.lower() == "y":
                        if stat_in.lower() == "s":
                            self.strength += amount_in
                            self.free_stat_points -= amount_in
                        elif stat_in.lower() == "v":
                            self.vitality += amount_in
                            self.free_stat_points -= amount_in
                        elif stat_in.lower() == "m":
                            self.magic += amount_in
                            self.free_stat_points -= amount_in
                        elif stat_in.lower() == "w":
                            self.will += amount_in
                            self.free_stat_points -= amount_in
                        elif stat_in.lower() == "d":
                            self.dexterity += amount_in
                            self.free_stat_points -= amount_in
                self.free_stat_points = 0
                self.recalculate_params()
                self.full_heal()
