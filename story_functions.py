import textwrap

from player import Player
import json
from textwrap import *


def create_character(room) -> Player:
    json_file_loc = "data/race_data.json"
    json_file = open(json_file_loc)
    races = json.load(json_file)
    json_file.close()
    cont = True
    player_name = ""
    player_gender = ""
    player_race = ""
    player_culture = ""
    player_trait = ""
    player_stats = []
    while cont:
        print(textwrap.fill("Hello, travelling soul. My name is Antheon, and will be assisting you in getting started "
                            "in Yasera.", 70))
        cont = False
        while not cont:
            name_cont = False
            while not name_cont:
                name = input("Now tell me, what is your name?\n> ")
                confirm = input(f"Is {name} what you wish to be called? Fear not, you can change it later if it no "
                                f"longer fits you.\n(y/n)> ")
                if 'y' == confirm.lower():
                    print(f"{name}... An interesting name. Let us continue.")
                    name_cont = True
                    player_name = name
                else:
                    print("Do not fear. We are in no rush.")
                    continue
            # TODO: add they/them gender support.
            gender_cont = False
            while not gender_cont:
                gender = input("Are you male or female? Once again, this can be changed later.\n(male/female)> ")
                if gender != "male" and gender != "female":
                    print("I'm sorry that gender is not yet supported. Please try again.")
                    continue
                confirm = input(f"Are you sure you wish to be {gender}?\n (y/n)> ")
                if confirm == 'y':
                    print("Excellent, let us continue.")
                    player_gender = gender
                    gender_cont = True
                else:
                    print("Do not fear. We are in no rush.")
                    continue
            # Race Support Time
            race_cont = False
            while not race_cont:
                print("Many races inhabit the land of Yasera. Here is a list, so you may choose which one you would "
                      "like to be.")
                for r in races["race"]:
                    print(r)
                print(fill("Each race has different cultures and people with different strengths and weaknesses. If you "
                      "would like a list of each culture, type in the race name. if you would like more details, "
                      "type in the race name and the culture name. When you are ready to make a choice, type\"choose "
                      "<race> <culture>\".",70))
                inp = False
                while not inp:
                    race_in = input("> ")
                    race_in = race_in.split(" ")
                    if race_in[0] != "choose":
                        if race_in[0] not in races["race"]:
                            print("I am not familiar with those people. Please try again.")
                            continue
                        else:
                            if len(race_in) == 1:
                                print("Cultures: ")
                                for c in races["race"][race_in[0]]["origin"]:
                                    print(c)
                                    continue
                            elif len(race_in) == 2:
                                if race_in[1] not in races["race"][race_in[0]]["origin"]:
                                    print("I am not familiar with those people. Please try again.")
                                    continue
                                else:
                                    temp = races["race"][race_in[0]]["origin"][race_in[1]]
                                    stats = races["race"][race_in[0]]["origin"][race_in[1]]["stats"]
                                    trait_name = races["race"][race_in[0]]["origin"][race_in[1]]["trait"]["name"]
                                    trait_desc = races["race"][race_in[0]]["origin"][race_in[1]]["trait"]["description"]
                                    print( + fill(temp["background"], 70))
                                    print(f"Starting stats: \nMagic: {stats[0]}\nStrength: {stats[1]}\nVitality: "
                                          f"{stats[2]}\nWill: {stats[3]}\nDexterity: {stats[4]}")
                                    print("Starter City: "+temp["suggested-city"])
                                    print(f"Trait:{trait_name}\nTrait description: {trait_desc}")
                                    continue
                            else:
                                print("I'm not sure what that means. Please try again")
                                continue
                    elif race_in[0] == "choose":
                        if race_in[1] not in races["race"]:
                            print("I am not familiar with those people. Please try again.")
                            continue
                        if race_in[2] not in races["race"][race_in[1]]["origin"]:
                            print("I am not familiar with those people. Please try again.")
                            continue
                        player_race = race_in[1]
                        player_culture = race_in[2]
                        inp = True
                confirm = input(f"You have chosen to become a {player_race} from the {player_culture}. Are you sure "
                                f"this is who you want to be? This cannot be changed later.\n(y/n)> ")
                if confirm == 'y':
                    print("Very well. Let us wrap this up. ")
                    race_cont = True
                else:
                    print("Do not worry, we have plenty of time.")
                    continue
            print(fill("We are now in the final stages before you are free to roam this world. First let us confirm "
                       "who you are.", 70))
            print(f"Name: {player_name}\nGender: {player_gender}\nRace: {player_race}\nCulture: {player_culture}.")
            confirm = input("Is this correct?\n(y/n)>")
            if confirm == 'y':
                print(f"Welcome, {player_name}, to Yasera!")
                cont = True
            else:
                print("Let us start over.")
                continue

        return Player(player_name, room, player_race, player_culture, player_gender, player_trait, player_stats)
