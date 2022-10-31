import typing
class Room:
    def __init__(self, room_id, desc, contents, enemies, exits:typing.List) -> None:
        self.room_id =room_id
        self.desc = desc
        self.contents = contents
        self.enemies = enemies
        self.exits = exits
    
    def start_encounter(self, player):
        print(f"Encounter: {player.name} vs. {str(self.enemies)[1:-2]}")
        first = None
        fastest_enemy = self.enemies[0]
        for e in self.enemies:
            if e.dexterity > fastest_enemy.dexterity:
                fastest_enemy = e
        if player.dexterity >= fastest_enemy.dexterity:
            first = player
        else:
            first = fastest_enemy
        fight_status = 0
        current_fighter = first
        while fight_status != 1:
            if current_fighter == player:
                attack = input("What would you like to do? (C)ast, (A)ttack, (F)lee.\n>")
                if attack.lower() == "c":
                    spell = print("Spells:")
                    temp_str = ""
                    for i,spell in enumerate(player.spells):
                        temp_str += (str(i) + ") "+spell.name + " \n")
                    cast = int(input(temp_str +"\n>"))
                    fight_status = player.cast(fastest_enemy,cast)
                    current_fighter = fastest_enemy
                elif attack.lower() == "f":
                    print("you run away")
                    return
            elif current_fighter == fastest_enemy:
                fastest_enemy.attack(player)
                current_fighter = player
                    
    
