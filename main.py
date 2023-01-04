import time
from random import randint
import gafu
from gafu import new_line, simple_divider, new_day_divider, read_delay, invalid_response
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

    popularity = 0  # ---- TODO Figure out what to do with Popularity
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
        plural = ""
        if increase > 1:
            plural ="s"
        print(f"**-- Your {trait} has increased {increase} point{plural}. --**")

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
            print(f"**-- Your grades in {subject} has increased {score} points. --**")


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

    friend_score = 0
    is_friend = False

    def increase_friend_score(self, score):
        self.friend_score += score

    def check_if_friends(self, player):
        if self.friend_score >= 10:
            self.is_friend = True

        if self.is_friend:
            return True, True
        else:
            if self.popularity < player.popularity:
                return False, True
            else:
                return False, False

    def check_if_fav_subject(self, subject):
        if subject == self.fav_subject:
            return True
        else:
            return False

    def check_if_bad_subject(self, subject):
        if subject == self.bad_subject:
            return True
        else:
            return False

    def __repr__(self):
        return self.name[1] + ' ' + self.name[0]


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

# ---- Club NPC Dictionaries ---- #
npc_dict = {"sports": [sport_npc_1, sport_npc_2], "video-games": [video_game_npc_1, video_game_npc_2],
            "theater": [theater_npc_1, theater_npc_2], "arts & crafts": [art_craft_npc_1, art_craft_npc_2],
            "dance": [dance_npc_1, dance_npc_2], "movie": [movie_npc_1, movie_npc_2]}

# ---- All NPCs in a single list for randomizing during events ---- #
npc_list = [npc for key, value in npc_dict.items() for npc in value]


###################################################
#   Main School Class - Everything happens here   #
###################################################

class School:
    def __init__(self, player):
        self.player = player

    skipping_class = False

    def classroom_event(self, subject):
        pass

    def library_event(self):
        random_npc = npc_list[randint(0, len(npc_list) - 1)]
        subject = ""

        def study_session(subject):
            study_buddy = False
            asked = False
            penalty = 0
            penalty_msg = ""

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
                        elif admire:  # ---- Your popularity was higher than theirs
                            print(
                                "They wouldn't normally, but your reputation makes them want to get to know you better.")
                            study_buddy = True
                            break
                        else:  # ---- You are shit out of luck and lose time
                            print("They barely look at you, as they pretend like they didn't hear you.")
                            penalty = 2
                            penalty_msg = f"Your focus is hurt by {random_npc}'s rejection."
                            print("Guess you're on your own.")
                            break
                    elif response == "n":
                        break
                else:
                    print("Sorry, that's an invalid choice")
                    new_line()

            read_delay()
            if asked:
                if study_buddy:
                    is_fav_subject = random_npc.check_if_fav_subject(subject)
                    is_bad_subject = random_npc.check_if_bad_subject(subject)
                    if is_fav_subject:
                        print(
                            f"{random_npc} has a natural passion for {subject}, and helps you grasp more of the knowledge.")
                        print("You both bonded over the experience!")
                        self.player.increase_grade(subject, 10)
                        random_npc.increase_friend_score(3)
                    elif is_bad_subject:
                        print(f"Turns out {subject} isn't {random_npc}'s best subject. Actually it's their worst.")
                        print(
                            "You both struggle to get through the textbook, but were able to use flash cards effectively.")
                        print("You bond a bit over the failure...")
                        self.player.increase_grade(subject, 4)
                        random_npc.increase_friend_score(2)
                    else:
                        print(
                            f"You study the {subject} textbook together, and {random_npc} helps you memorize more than you normally do.")
                        print("They like you a bit more!")
                        self.player.increase_grade(subject, 7)
                        random_npc.increase_friend_score(2)
                else:
                    print("You find a quiet part of the library and open up your textbooks. It's a slow read.")
                    print(penalty_msg)
                    self.player.increase_grade(subject, 5 - penalty)
            else:
                print("You find a quiet part of the library and open up your textbooks. It's a slow read.")
                self.player.increase_grade(subject, 5)

        library_event = 0
        # ---- Enter the library
        new_line()
        print("You come into the library. It has a calm and quiet atmosphere.")
        new_line()
        while True:
            possible_answers = ["1", "2"]
            print("Do you want to study or work on your focus? \n(1) - Study Session \n(2) - Work on Focus")
            response = input("")
            if response in possible_answers:
                if response == "1":
                    library_event = 1
                    break
                elif response == "2":
                    library_event = 2
                    break
            else:
                invalid_response()
            #  ---- Study Session or Raise Focus trait
        if library_event == 1:  # ---- Study Session Event
            picked_subject = False
            while not picked_subject:
                possible_answers = ["1", "2", "3", "4", "5", "6"]
                possible_subjects = [key for key in subject_dict.keys()]
                while True:
                    print("Which subject would you like to study?")
                    counter = 1
                    for sub in possible_subjects:
                        print(f"{sub} - ({counter})")
                        counter += 1
                    print("( 1 / 2 / 3 / 4 / 5 / 6 )")
                    response = input("")
                    if response in possible_answers:
                        if response == "1":
                            subject = possible_subjects[0]
                            picked_subject = True
                            break
                        elif response == "2":
                            subject = possible_subjects[1]
                            picked_subject = True
                            break
                        elif response == "3":
                            subject = possible_subjects[2]
                            picked_subject = True
                            break
                        elif response == "4":
                            subject = possible_subjects[3]
                            picked_subject = True
                            break
                        elif response == "5":
                            subject = possible_subjects[4]
                            picked_subject = True
                            break
                        elif response == "6":
                            subject = possible_subjects[5]
                            picked_subject = True
                            break
                    else:
                        print("Sorry, that was an invalid response. Try again.")
                        new_line()
                        time.sleep(1)

            new_line()
            print(f"You see {random_npc} sitting at one of the desks, reading a textbook.")
            study_session(subject)  # ---- Starts Study Session Event

        elif library_event == 2:  # ---- Raise Focus trait Event
            print("You pick out a book from the self-help section.")
            if not self.skipping_class:
                self.player.increase_trait("Focus", 1)
            elif self.skipping_class:
                self.player.increase_trait("Focus", 2)

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

        test_player = Player("Steven", {"physique": 4, "focus": 4, "creativity": 4}, ["American Football"])
        school = School(test_player)
        read_delay()

        school.classroom_event("Math")


game = Game()

if __name__ == "__main__":
    game.run()
