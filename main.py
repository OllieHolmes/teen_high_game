from random import randint
import gafu
from gafu import new_line, simple_divider, new_day_divider, read_delay
from hobbies import hobby_dict
import story

# ---- Help objects that store static information

grades_dict = {"A": 40, "B": 30, "C": 20, "F": 0}

subject_dict = ({"English": "Creativity", "Math": "Focus", "Science": "Creativity",
                 "Physical Education": "Physique", "Computer Science": "Focus", "Health Studies": "Physique"})


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

    def display_status(self):
        print(f"Your hobbies are {self.repr_hobbies(self.hobbies)}.")
        print(f"Your traits are:")
        for hobby in self.hobbies:
            print(f"- {hobby}")


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
    counter = randint(0, 1)
    def __init__(self):
        xx = False
        if self.counter % 2 == 0:
            xx = False
        else:
            xx = True
        self.name = gafu.generate_name(xx)
        Student.counter += 1

class StudentNPC(Student):
    def set_popularity(self):
        pass

    def __init__(self, club, fav_subject, bad_subject):
        hobbies = gafu.assign_npc_hobbies(club)
        super().__init__()
        self.club = club
        self.fav_subject = fav_subject
        self.fav_trait = subject_dict[fav_subject]
        self.bad_subject = bad_subject
        self.bad_trait = subject_dict[bad_subject]
        self.hobbies = [h for h in hobbies]
        self.popularity = randint(10, 40)

    def __repr__(self):
        return self.name[1] + ' ' + self.name[0]


###################################################
#   Main School Class - Everything happens here   #
###################################################

# ---- NPC information and Data
sport_npc_1 = StudentNPC("sports", "Physical Education", "English")
sport_npc_2 = StudentNPC("sports", "Health Studies", "Math")
video_game_npc_1 = StudentNPC("video-games", "Computer Science", "English")
video_game_npc_2 = StudentNPC("video-games", "Science", "Math")
theater_npc_1 = StudentNPC("theater", "English", "Math")
theater_npc_2 = StudentNPC("theater", "Science", "Computer Science")
art_craft_npc_1 = StudentNPC("arts & crafts", "English", "Health Studies")
art_craft_npc_2 = StudentNPC("arts & crafts", "Science", "Physical Education")
dance_npc_1 = StudentNPC("dance", "Physical Education", "Math")
dance_npc_2 = StudentNPC("dance", "Health Studies", "Computer Science")
movie_npc_1 = StudentNPC("movie", "Computer Science", "Physical Education")
movie_npc_2 = StudentNPC("movie", "Math", "Health Studies")

npc_dict = {"sports": [sport_npc_1, sport_npc_2], "video-games": [video_game_npc_1, video_game_npc_2],
            "theater": [theater_npc_1, theater_npc_2], "arts & crafts": [art_craft_npc_1, art_craft_npc_2],
            "dance": [dance_npc_1, dance_npc_2], "movie": [movie_npc_1, movie_npc_2]}

npc_list = [npc for key, value in npc_dict.items() for npc in value]


class School:

    def library_event(self, player):
        # ---- Enter the library
        print("You come into the library and sit down to study.")

    def break_event(self, player):
        pass

    def cafeteria_event(self, type_of_meal, player):
        pass


class Game:

    def run(self):
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

        school = School()

        # ----- Create the Player Character
        player_name = gafu.name_the_player()
        story.welcome_to_teen_high(player_name)
        starting_traits = gafu.choose_starting_traits()
        simple_divider()
        starting_hobby = gafu.choose_starting_hobbies()
        player_1 = Player(player_name, starting_traits, starting_hobby)

        print(player_1)
        simple_divider()

        # ----- Introduction Message

        new_day_divider()
        story.start_of_day(1)


game = Game()

if __name__ == "__main__":
    game.run()