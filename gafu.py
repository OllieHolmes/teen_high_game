from names import boys_names, girls_names, surnames
from hobbies import hobby_list
from random import randint

# ----- Text Functions -----
def new_line(num=1):
    for n in range(num):
        print("")

def simple_divider():
    print("#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#")

def new_day_divider():
    print("**********************************************************************************************************")
    print("------------------------------------------------  NEW DAY  -----------------------------------------------")
    print("**********************************************************************************************************")



# ----- NPC Generators -----
def generate_name(xx=False):
    rand_last = randint(0, len(surnames) - 1)
    if xx == False:
        rand_first = randint(0, len(girls_names) - 1)
        new_name = (surnames[rand_last], girls_names[rand_first])
    else:
        rand_first = randint(0, len(boys_names) - 1)
        new_name = (surnames[rand_last], boys_names[rand_first])
    return new_name


def assign_npc_hobbies(hobby_type):
    npc_hobbies = {"main": [], "secondary": []}
    hobby_list_keys = list(hobby_list.keys())
    num_of_hobbies = randint(1, 3)
    hobby_num = randint(0, len(hobby_list[hobby_type]) - 1)
    npc_hobbies["main"] = [hobby_type, hobby_list[hobby_type][hobby_num]]
    for n in range(num_of_hobbies):
        hobby_cat_num = randint(0, len(hobby_list) - 1)
        hobby_cat = hobby_list_keys[hobby_cat_num]
        hobby_num = randint(0, len(hobby_list[hobby_cat]) - 1)
        npc_hobbies["secondary"].append([hobby_cat, hobby_list[hobby_cat][hobby_num]])
    return npc_hobbies



# ----- Player Creator -----
def name_the_player():
    player_name = input("What is your name? ")
    return player_name


def choose_player_traits():
    print(
        '''
        There are 3 different traits that help you on your high school adventure:
        Physique, Focus and Creativity.
        All clubs have a main trait, and a secondary trait which will help you raise your popularity.
        Physique is the main trait of the Sports Club, and the Dance Club.
        Focus is the main trait of the Video Game Club, and the Movie Club.
        Creativity is the main trait of the Theater Club, and the Arts & Crafts Club
        You get to start off with 2 points in one trait and 1 point in a second trait.
        '''
    )

    def assign_traits():
        phys_score = 0
        focus_score = 0
        creativity_score = 0
        player_happy = False
        while player_happy == False:
            while True:
                possible_response = {"p": "Physique", "f": "Focus", "c": "Creativity"}
                response = input(
                    "Which trait would you like to give 2 points? \nPhysique - (p) \nFocus - (f) \nCreativity - (c) \n")
                if response in possible_response:
                    if response == "p":
                        phys_score = 2
                        possible_response.pop(response)
                    elif response == "f":
                        focus_score = 2
                        possible_response.pop(response)
                    elif response == "c":
                        creativity_score = 2
                        possible_response.pop(response)
                    break
                else:
                    print("Sorry that's an invalid choice. Try again.")
            while True:
                choices_left = list(possible_response.keys())
                response = input(
                    "Which trait would you like to give 1 point? \n{first} - ({first_let}) \n{second} - ({second_let})\n".format(
                        first=possible_response[choices_left[0]], first_let=choices_left[0],
                        second=possible_response[choices_left[
                            1]], second_let=choices_left[1])
                )

                if response in possible_response:
                    if response == "p":
                        phys_score = 1
                    elif response == "f":
                        focus_score = 1
                    elif response == "c":
                        creativity_score = 1
                    break
                else:
                    print("Sorry that's an invalid choice. Try again.")
            while True:
                print("You have chosen: \nPhysique - {physique} \nFocus - {focus} \nCreativity - {creativity}".format(
                    physique=phys_score, focus=focus_score, creativity=creativity_score))
                happy = input("Are you happy with that choice? \n(y/n) ")
                possible_response = ["y", "n"]
                if happy in possible_response:
                    if happy == "y":
                        player_happy = True
                        break
                    else:
                        break
                else:
                    "Sorry that's an invalid choice. Try again."
        return phys_score, focus_score, creativity_score

    phys, focus, creativity = assign_traits()
    player_traits = {"physique": phys, "focus": focus, "creativity": creativity}
    return player_traits


def choose_starting_hobbies():
    hobby_list_keys = list(hobby_list.keys())
    available_choices = []
    for key in range(len(hobby_list_keys)):
        rand_hobby = randint(0, len(hobby_list[hobby_list_keys[key]]) - 1)
        available_choices.append(hobby_list[hobby_list_keys[key]][rand_hobby])
    print("You also get to start with a hobby that will help you bond with your fellow students. \n")

    def make_decision():
        happy_with_choice = False
        while happy_with_choice == False:
            possible_choices = ["1", "2", "3", "4", "5", "6"]
            print("Your choices are:")
            counter = 1
            for choice in available_choices:
                print(f"({counter}) - " + choice)
                counter += 1
            while True:
                response = input("Which one do you want to start with? \n( 1 / 2 / 3 / 4 / 5 / 6 ) \n")
                if response in possible_choices:
                    if response == "1":
                        player_hobby = available_choices[0]
                        break
                    elif response == "2":
                        player_hobby = available_choices[1]
                        break
                    elif response == "3":
                        player_hobby = available_choices[2]
                        break
                    elif response == "4":
                        player_hobby = available_choices[3]
                        break
                    elif response == "5":
                        player_hobby = available_choices[4]
                        break
                    elif response == "6":
                        player_hobby = available_choices[5]
                        break
                else:
                    "Sorry that's an invalid response. Try again."
            while True:
                possible_choices = ["y","n"]
                response = input(f"You have chosen {player_hobby}. Are you sure? \n(y/n) \n")
                if response in possible_choices:
                    if response == "y":
                        happy_with_choice = True
                        break
                    elif response == "n":
                        break
                else:
                    print("Sorry, that's an invalid choice. Try again.")
        return player_hobby

    player_hobby = make_decision()

    return player_hobby

if __name__ == "__main__":

    simple_divider()
    new_line()
    new_day_divider()
