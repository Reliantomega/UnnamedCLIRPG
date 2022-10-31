from math import *

class Spell:
    def __init__(self, element, name, range = 0, multitarget=False, radius = 0, num_targets = 0):
        #Elemental affinity: Fire, Water, Earth, Wind, Dark, Light, and Kenetic.
        self.element = element
        # Range of spell: square law, the farther the distance the more expensive, except for Light and Dark spells. 
        # Light has a miniscule linear progression, Dark has a quadratic increase in MP.
        self.range = range
        # Multi Target means that it can hit multiple targets. if radius is 0, then it is targeted and will have a higher cost
        # if num_target is 0 then it hits everything in a radius. if both have a number, then it is target aoes, which ahs a multiplicitive
        # effect on costs.
        self.multi_target = multitarget
        # AOE radius effects will reduce indiviual damage on targets but will hit all in that radius. Follows a linear drop off
        self.radius = radius
        # targets individual targets, retaining damage but causing the overall complexity of the spell to double per added target, exponentially
        self.num_targets = num_targets
        # Complexity is a function of the different aspects of a spell, and affects the cost. Follows a shallow exponental curve. 
        # e^.05x
        self.complexity = 0
        self.cost = 0
        self.damage = 0
        self.name = name
        # Elements and their base complexity cost
        elements = {"f":2,"w":4,"e":5,"a":3,"l":10,"d":10, "k":8}
        # Add elemental complexity
        self.complexity += elements[element]
        # add range complexity. 0 rane is a touch or self spell
        self.complexity += range*2
        if multitarget:
            if num_targets > 0 and radius > 0:
                self.complexity += (self.complexity * pow(2, num_targets))+(self.complexity/(pi * pow(radius,2)))
            elif num_targets > 0 and radius == 0:
                self.complexity += self.complexity * pow(2, num_targets)
            elif radius > 0 and num_targets == 0:
                self.complexity += self.complexity/(pi * pow(radius,2))
        # Damage and cost is a function of complexity
        self.damage = floor(self.complexity*.8)
        self.cost = floor(self.complexity*.5)

    def print_spell_details(self):
        print(f"damage: {self.damage}\ncost: {self.cost}\nComplexity: {self.complexity}")


