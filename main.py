from random import randint
import gafu
from gafu import new_line, simple_divider, new_day_divider

subjects = ({"English": "Creativity", "Math": "Focus", "Science": "Creativity",
             "Physical Education": "Physique", "Computer Science": "Focus", "Health Studies": "Physique"})

npc_dict = {"sports": [], "video-games": [], "theater": [], "arts & crafts": [], "dance": [], "literature": [],
            "movie": []}


class Player:
    def __init__(self):
        self.name = "Name function"
        self.traits = {"physique": 2, "focus": 1, "creativity": 0}
        self.hobbies = ["hobby 1", "hobby 2"]
        self.popularity = 0

    def print_hobbies(self, hobby_list):
        message = ""
        for hobby in hobby_list:
            if hobby == hobby_list[len(hobby_list) - 1]:
                message += hobby
            else:
                message += hobby + ", "
        return message

    def print_traits(self, traits_dict):
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
        return (f"You are {self.name}, a high school student. Your hobbies are {self.print_hobbies(hobby_list)}.\n" +
                f"Your traits are {self.print_traits(traits_dict)}"
                )


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
# Main School Class - Everything gets stored here #
###################################################
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




# if __name__ == "__main__":
#     Game.run()
