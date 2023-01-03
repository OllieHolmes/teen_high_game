import time
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

    popularity = 50  # ---- TODO Figure out what to do with Popularity
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

    is_friend = False

    def check_if_friends(self, player):
        if self.is_friend:
            return True, True
        else:
            if self.popularity < player.popularity:
                return False, True
            else:
                return False, False


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
    def __init__(self, player):
        self.player = player

    def library_event(self):
        random_npc = npc_list[randint(0, len(npc_list) - 1)]
        # ---- Enter the library
        new_line()
        print("You come into the library and sit down to study.")
        print(f"You see {random_npc} sitting at one of the desks, reading a textbook.")
        new_line()

        def study_session(subject):
            study_buddy = False
            asked = False

            while True:
                response = input(f"Do you want to ask {random_npc} to study with you? \n(y/n) ")
                possible_answers = ["y", "n"]
                if response in possible_answers:
                    if response == "y":  # ---- Player chooses to ask the NPC
                        print(f"You ask {random_npc} if they would like to study with you.")
                        asked = True
                        friends, admire = random_npc.check_if_friends(self.player)
                        if friends:  # ---- Friends help each other out
                            print("Since you're good friends, they gladly accept.")
                            study_buddy = True
                            break
                        elif admire: # ---- Your popularity was higher than theirs
                            print("They wouldn't normally, but your reputation makes them want to get to know you better.")
                            study_buddy = True
                            break
                        else:  # ---- You are shit out of luck
                            print("They barely look at you, as they pretend like they didn't hear you.")
                            print("Guess you're on your own.")
                            read_delay()
                            break
                    elif response == "n":
                        break
                else:
                    print("Sorry, that's an invalid choice")
                    new_line()

            if asked:
                if study_buddy:

                    pass  # ---- Run a function to check if the study buddy helps
            else:
                pass  # ---- You study on your own and get the basic bonus

        study_session("Health Studies")



    def break_event(self):
        pass

    def cafeteria_event(self, type_of_meal):
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



        # ----- Create the Player Character
        # player_name = gafu.name_the_player()
        # story.welcome_to_teen_high(player_name)
        # starting_traits = gafu.choose_starting_traits()
        # simple_divider()
        # starting_hobby = gafu.choose_starting_hobbies()
        # player_1 = Player(player_name, starting_traits, starting_hobby)  # ---- Instancing the player
        #
        # school = School(player_1)  # ---- Instancing the School class, which contains all basic events
        #
        # print(player_1)
        # simple_divider()
        #
        #
        # # ----- Introduction Message
        #
        # new_day_divider()
        # story.start_of_day(1)

        player_test = Player("Steven", {"physique": 4, "focus": 4, "creativity": 4}, ["American Football"])
        school = School(player_test)
        read_delay()
        read_delay()
        read_delay()
        read_delay()

        school.library_event()


game = Game()

if __name__ == "__main__":
    game.run()
