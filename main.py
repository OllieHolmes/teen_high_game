from random import randint
import gafu
from gafu import new_line, simple_divider, new_day_divider
from hobbies import hobby_dict
import story

# ---- Help objects that store static information and npc data

subject_dict = ({"English": "Creativity", "Math": "Focus", "Science": "Creativity",
                 "Physical Education": "Physique", "Computer Science": "Focus", "Health Studies": "Physique"})

npc_dict = {"sports": [], "video-games": [], "theater": [], "arts & crafts": [], "dance": [], "literature": [],
            "movie": []}

npc_random_list = []


# ---- Main Player Class ----

class Player:
    def __init__(self, name, traits, hobby):
        self.name = name
        self.traits = traits
        self.hobbies = [hobby]

    popularity = 0
    grades = {"English": 0, "Math": 0, "Science": 0,
              "Physical Education": 0, "Computer Science": 0, "Health Studies": 0}

    def repr_hobbies(self, hobby_list):
        message = ""
        for hobby in hobby_list:
            if hobby[1] == hobby_list[len(hobby_list) - 1][1]:
                message += hobby[1]
            else:
                message += hobby[1] + ", "
        return message

    def repr_traits(self, traits_dict):
        message = ""
        traits_list = [trait for trait in traits_dict.keys()]
        for trait in traits_dict:
            if trait == traits_dict[traits_list[-1]]:
                message += f"{trait.title()} = {traits_dict[trait]}"
            else:
                message += f"{trait.title()} = {traits_dict[trait]}, "
        return message

    def __repr__(self):
        hobby_list = self.hobbies
        traits_dict = self.traits
        return (f"You are {self.name}, a high school student. Your hobbies are {self.repr_hobbies(hobby_list)}.\n" +
                f"Your traits are {self.repr_traits(traits_dict)}"
                )

    # ---- Functions that add functionality to the player

    def increase_trait(self, trait, increase=1):
        self.traits[trait.lower()] += increase

    def decrease_trait(self, trait, decrease=1):
        self.traits[trait.lower()] -= decrease

    def add_hobby(self, hobby):
        hobby = hobby.title()
        if hobby in self.hobbies:
            print("You already have that hobby! \nLooks like you wasted your time.")
            return

        hobby_exist = False
        hobby_key = ""
        for key, values in hobby_dict.items():
            if hobby in values:
                hobby_exist = True
                hobby_key = key

        if hobby_exist:
            self.hobbies.append([hobby_key, hobby])
            print(f"You've added {hobby} to your list of hobbies. Good job!")
            return

    def increase_grade(self, subject, score):
        if subject in subject_dict:
            self.grades[subject] += score
            print(f"Your grades in {subject} has increased.")


class Student:
    def __init__(self):
        self.name = gafu.generate_name()

    def __repr__(self):
        return "This is " + self.name[1] + ' ' + self.name[0] + ". They're a student here."


class StudentNPC(Student):
    def set_popularity(self):
        pass

    def __init__(self, hobbies):
        super().__init__()
        self.fav_subject = "fav subject"
        self.bad_subject = "bad subject"
        self.hobbies = [h for h in hobbies]
        self.popularity = 0


class Classroom:
    pass



###################################################
#   Main School Class - Everything happens here   #
###################################################

class School:

    def library_event(self, player):
        # ---- Enter the library
        print("You come into the library and sit down to study.")

    def break_event(self, player):
        pass

    def cafeteria_event(self, type_of_meal, player):
        pass


class Game:

    def run():
        print("""
        ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
          ####### ######  ###### #      #     #     #  #    ####    #     #
             #    #       #      # #    #     #     #  #   #    #   #     #
             #    #       #      #  #   #     #     #  #  #         #     #
             #    #####   #####  #   #  #     #######  #  #    ##   #######
             #    #       #      #    # #     #     #  #  #     #   #     #
             #    #       #      #     ##     #     #  #   #   ##   #     #
             #    ######  ###### #      #     #     #  #    ### #   #     #
        ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤ 
                                The High School Simulator
        ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤""")

        # ----- The Game Starts Here ----- #

        # ----- Create the Player Character
        player_name = gafu.name_the_player()
        starting_traits = gafu.choose_starting_traits()
        new_line()
        starting_hobby = gafu.choose_starting_hobbies()
        player_1 = Player(player_name, starting_traits, starting_hobby)

        print(player_1)
        gafu.read_delay()
        simple_divider()

        story.welcome_to_teen_high(player_1.name)


if __name__ == "__main__":
    Game.run()


