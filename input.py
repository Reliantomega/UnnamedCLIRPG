# from math import *
from textwrap import TextWrapper
from player import Player
from story_functions import *
from spell import *
from spell_list import *
from room_list import *
import typing


player_obj: Player = create_character(room_list[0])

json_file_loc = "data/race_data.json"
# player_obj = create_character()
# player_obj = Player("Tetra",room_list[0])
# player_obj.jobs.append("mage")
player_obj.print_params()

player_obj.learn_spell(spell_list["air blast"])

# for spell in player_obj.spells:
#     spell.print_spell_details()
# player_obj.level_up()
# player_obj.level_up()
# player_obj.level_up()
# player_obj.level_up()

player_obj.print_params()

# commands = {
#     "level up": player_obj.level_up(),
#     "examine room": player_obj.examine_room(),
#     "meditate": player_obj.meditate()
# }
cont = True
print("What do you want to do?")
while cont:
    inp = input("> ")
    if inp == "level":
        player_obj.level_up()
    elif inp == "examine room":
        player_obj.examine_room()
    elif inp == "meditate":
        player_obj.meditate()
    elif inp == "status":
        player_obj.print_params()
    elif inp == "take damage":
        player_obj.take_damage(5)
    elif inp == "heal":
        player_obj.full_heal()
    elif inp == "attack":
        player_obj.current_room.start_encounter(player_obj)
    elif inp == "quit":
        cont = False