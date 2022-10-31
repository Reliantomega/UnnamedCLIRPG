from math import *

class Skill:
    #Skills are passive abilities
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.level = 1
        