import time
from random import randint
import gafu
from gafu import new_line, simple_divider, new_day_divider, read_delay, invalid_response
from hobbies import hobby_dict
import story

# ---- Help objects that store static information

grades_dict = {"A": 40, "B": 30, "C": 20, "F": 0}

subject_dict = {"English": "Creativity", "Math": "Focus", "Science": "Creativity",
                "Physical Education": "Physique", "Computer Science": "Focus", "Health Studies": "Physique"}


# ---- Player & NPC Classes ----
class Player:
    def __init__(self, name, traits, hobby):
        self.name = name
        self.traits = traits
        self.hobbies = [hobby]

    popularity = 7
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
            plural = "s"
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
    popularity_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    def __init__(self, club, fav_subject, bad_subject):
        hobbies = gafu.assign_npc_hobbies(club)
        rand_popularity = randint(0, len(self.popularity_list) - 1)
        super().__init__()
        self.club = club
        self.fav_subject = fav_subject
        self.fav_trait = subject_dict[fav_subject]
        self.bad_subject = bad_subject
        self.bad_trait = subject_dict[bad_subject]
        self.hobbies = [hobbies["main"][1]] + [value[1] for value in hobbies["secondary"]]
        self.advanced_hobbies = hobbies
        self.popularity = self.popularity_list.pop(rand_popularity)
        self.clue_list = []

    friend_score = 0
    is_friend = False

    def add_clue(self, clue):
        hobby_reference = [x for key, value in hobby_dict.items() for x in value]
        if clue in subject_dict:
            if clue + " +" in self.clue_list or clue + " -" in self.clue_list:
                return True
            else:
                if clue == self.fav_subject:
                    self.clue_list.insert(0, clue + " +")
                    print(f"**-- You discovered that {self.name[1]} is good at {clue} --**")
                elif clue == self.bad_subject:
                    self.clue_list.insert(0, clue + " -")
                    print(f"**-- You discovered that {self.name[1]} is bad at {clue} --**")
        elif clue in hobby_reference:
            if clue in self.hobbies:
                done = False
                counter = 0
                check_clue = self.hobbies[counter]
                while not done:
                    if check_clue in self.clue_list:
                        counter += 1
                        try:
                            check_clue = self.hobbies[counter]
                        except IndexError:
                            print(f"Looks like you already know all of {self.name[1]}'s hobbies.")
                            done = True
                    else:
                        self.clue_list.insert(-1, check_clue)
                        print(f"**-- You discovered that {self.name[1]} likes {check_clue} --**")
                        done = True

    def increase_friend_score(self, score):
        self.friend_score += score

    def check_if_friends(self, player):
        if self.friend_score >= 10:
            self.is_friend = True

        if self.is_friend:
            return True, True
        else:
            if gafu.popularity_check(player, self):
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
        clues = ""
        for clue in self.clue_list:
            clues += f"({clue}), "
        clue_message = ""
        if self.clue_list != []:
            clue_message = " [" + clues + "]"
        return self.name[1] + ' ' + self.name[0] + clue_message


######################################################################################################
#                                     Everything happens here                                        #
######################################################################################################

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

# ---- Put NPCs into Classrooms
english_group = []
math_group = []
science_group = []
pe_group = []
cs_group = []
health_group = []
all_class_groups = [english_group, math_group, science_group, pe_group, cs_group, health_group]
all_npcs_sorted = list(npc_list)

for group in all_class_groups:
    rand_num = randint(0, len(all_npcs_sorted) - 1)
    group.append(all_npcs_sorted.pop(rand_num))
    rand_num = randint(0, len(all_npcs_sorted) - 1)
    group.append(all_npcs_sorted.pop(rand_num))
for i in range(len(all_class_groups)):
    rand_student = randint(0, 1)
    all_class_groups[i].append(all_class_groups[-(i + 1)][rand_student])
class_by_subject = {"English": english_group, "Math": math_group, "Science": science_group,
                    "Physical Education": pe_group, "Computer Science": cs_group, "Health Studies": health_group}

# ---- Create a list of the most popular NPCs and Clubs
popular = [(npc, npc.popularity) for npc in npc_list]
most_popular_list = sorted(popular, key=lambda x: x[1], reverse=True)
clubs_by_popularity = [(key, (value[0].popularity + value[1].popularity) / 2) for key, value in
                       npc_dict.items()]
clubs_by_popularity.sort(key=lambda x: x[1], reverse=True)  # ---- Highest popularity first.


def update_most_popular():
    global most_popular_list
    global clubs_by_popularity

    popular = [(npc, npc.popularity) for npc in npc_list]
    most_popular_list = sorted(popular, key=lambda x: x[1], reverse=True)

    clubs_by_popularity = [(key, (value[0].popularity + value[1].popularity) / 2) for key, value in
                           npc_dict.items()]
    clubs_by_popularity.sort(key=lambda x: x[1], reverse=True)  # ---- Highest popularity first.


######################################################################################################
#                                            All Events                                              #
######################################################################################################

skipping_class = False


# ---- Finished ++++++
def classroom_event(player, subject):
    global skipping_class
    update_most_popular()
    classroom = class_by_subject[subject]
    print(f"            #######################  {subject} Class  #########################")
    new_line()
    print("You enter the classroom and you see that most tables are full.")
    print("There are 4 tables with open seats.")
    new_line()
    print(
        f"Do you want to sit next to \n(1) {classroom[0]} \n(2) {classroom[1]} \n(3) {classroom[2]} \n(4) sit by yourself?")
    seat = ""
    # --- Choose seat ---- #
    while True:
        possible_answers = ["1", "2", "3", "4"]
        response = input("( 1 / 2 / 3 / 4 ) \n")
        if response in possible_answers:
            if response == "1":
                seat = classroom[0]
                break
            elif response == "2":
                seat = classroom[1]
                break
            elif response == "3":
                seat = classroom[2]
                break
            elif response == "4":
                seat = "alone"
                break
        else:
            invalid_response()

    # ---- Checks if the subject is one of the NPCs fav or bad subject ---- #
    if response != "4":
        print(f"You sit down next to {seat.name[1]}.")
        if seat.is_friend:
            print(
                "As you take a seat next to them, they visibly relax and it is clear that they are happy that you chose to sit with them.")
        else:
            print("They move over a bit as you sit down, as to not sit too close.")

        if subject == seat.fav_subject:
            print(f"You can tell that {seat.name[1]} is passionate about {subject}")
            new_line()
            clue_found = seat.add_clue(subject)
            print(f"{seat.name[1]} helps you out throughout the class, and you feel smarter when class is over.")
            new_line()
            if clue_found:
                pass
            else:
                player.increase_trait(subject_dict[subject], 1)
            player.increase_grade(subject, 7)
        elif subject == seat.bad_subject:
            print(f"{seat.name[1]} is clearly not great at {subject}.")
            seat.add_clue(subject)
            new_line()
            print("They struggle throughout the whole class disrupting your focus.")
            player.increase_grade(subject, 3)
        else:
            print(f"You listen to the lecture and work with {seat.name[1]}.")
            seat.add_clue(subject)
            new_line()
            print(f"It's just a regular {subject} class.")
            player.increase_grade(subject, 5)

        if player.popularity > seat.popularity:
            new_line()
            print(f"After the class {seat.name[1]} comes up and chats for a bit.")
            while True:
                response = input("Do you want to stay and chat with them? \n(y/n) ")
                possible_answers = ["y", "n"]
                if response in possible_answers:
                    if response == "y":
                        print(
                            f"You stay and talk for a bit about your hobbies. You feel closer to {seat.name[1]} {seat.name[0]}.")
                        seat.increase_friend_score(5)
                        seat.add_clue(seat.hobbies[0])
                        break
    else:
        print("You're in luck, there's one empty table, and you snag it.")
        print(
            "You focus all of your attention on the lecture, and finish up all the workbook questions with time to spare.")
        print("You decide to even do a few extra credit questions.")
        player.increase_grade(subject, 8)

    read_delay()
    simple_divider()
    skipping_class = False


# ---- Finished ++++++
def library_event(player):
    global skipping_class
    update_most_popular()
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
                    print(f"You ask {random_npc.name[1]} if they would like to study with you.")
                    asked = True
                    friends, admire = random_npc.check_if_friends(player)
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
                        penalty_msg = f"Your focus is hurt by {random_npc.name[1]}'s rejection."
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
                        f"{random_npc.name[1]} has a natural passion for {subject}, and helps you grasp more of the knowledge.")
                    clue_found = random_npc.add_clue(subject)
                    print("You both bonded over the experience!")
                    if clue_found:
                        pass
                    else:
                        player.increase_trait(subject_dict[subject], 1)
                    player.increase_grade(subject, 10)
                    random_npc.increase_friend_score(3)
                elif is_bad_subject:
                    print(
                        f"Turns out {subject} isn't {random_npc.name[1]}'s best subject. Actually it's their worst.")
                    print(
                        "You both struggle to get through the textbook, but were able to use flash cards effectively.")
                    random_npc.add_clue(subject)
                    print("You bond a bit over the failure...")
                    player.increase_grade(subject, 4)
                    random_npc.increase_friend_score(2)
                else:
                    print(
                        f"You study the {subject} textbook together, and {random_npc.name[1]} helps you memorize more than you normally do.")
                    print("They like you a bit more!")
                    player.increase_grade(subject, 7)
                    random_npc.increase_friend_score(2)
            else:
                print("You find a quiet part of the library and open up your textbooks. It's a slow read.")
                print(penalty_msg)
                player.increase_grade(subject, 5 - penalty)
        else:
            print("You find a quiet part of the library and open up your textbooks. It's a slow read.")
            player.increase_grade(subject, 5)

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
        if not skipping_class:
            print("You pick out a book from the self-help section that has some small bites of motivational tips.")
            player.increase_trait("Focus", 1)
        elif skipping_class:
            print("You find a chess board in the library and meticulously play a game against yourself.")
            player.increase_trait("Focus", 2)

    read_delay()
    skipping_class = False


# ---- Finished ++++++
def gymnasium_event(player):
    global skipping_class
    # ---- Enter the Gym
    new_line()
    print("You walk into the gym. It smells like teenage sweat, \n"
          "and you can hear the telltale sound of rubber shoes on linoleum.")
    new_line()
    # ---- Raise Physique trait Event

    if not skipping_class:
        print("You line yourself up along the basketball court and do a few laps of high intensity laps.")
        player.increase_trait("Physique", 1)
    elif skipping_class:
        print("You make your way over to the free-weights and do a full workout set.")
        player.increase_trait("Physique", 2)

    skipping_class = False
    read_delay()

# ---- Finished ++++++
def art_room_event(player):
    global skipping_class
    # ---- Enter the Art Room
    new_line()
    print("You make your way to the art room, and you find it in a state of creative chaos. \n"
          "Or maybe it's just a big mess. However, plenty of art supplies are left out for you to play with.")
    new_line()
    # ---- Raise Creativity trait Event

    if not skipping_class:
        print("Since you're strapped for time, you grab an (almost) blank canvas "
              "and let your inner Pollock out on the white sheet.")
        player.increase_trait("Creativity", 1)
    elif skipping_class:
        print("You find some clay and sit down to sculpt your next masterpiece.")
        player.increase_trait("Creativity", 2)

    skipping_class = False
    read_delay()


# ---- Not Finished
def cafeteria_event(player, type_of_meal):
    update_most_popular()
    print(f"           #########################  {type_of_meal} Class  #########################")
    new_line()


# ---- Not Started
def break_event(player, type_of_break):
    update_most_popular()
    print(f"           #########################  {type_of_break}  #########################")
    new_line()


class Game:

    @classmethod
    def run(cls):
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
        # print(player_1)
        # simple_divider()
        #
        #
        # # ----- Introduction Message
        #
        # new_day_divider()
        # story.start_of_day(1)

        test_player = Player("Steven", {"physique": 4, "focus": 4, "creativity": 4}, ["American Football"])
        test_list = gafu.assign_npc_hobbies("sports")

        break_event(test_player, "Recess")
        classroom_event(test_player, "Math")
        library_event(test_player)
        gymnasium_event(test_player)
        art_room_event(test_player)

if __name__ == "__main__":
    Game.run()
