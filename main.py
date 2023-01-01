from random import randint
import gafu

npc_dict = {"sports": [], "video-games": [], "theater": [], "arts & crafts": [], "dance": [], "literature": [],
            "movie": []}


class Student:
    def __init__(self):
        self.name = gafu.generate_name()

    def __repr__(self):
        return "This is " + self.name[1] + ' ' + self.name[0] + ". They're a student here."


class Player:
    def __init__(self):
        self.name = "Name function"
        self.stats = "Stats function"
        self.hobbies = "Hobby function"
        self.popularity = 0


class StudentNPC(Student):
    def __init__(self, stats, hobbies):
        super().__init__()
        self.stats = "npc stats function"
        self.hobbies = [h for h in hobbies]
        self.popularity = 0


class Classroom:
    pass


test = StudentNPC("s", "h")
print()
print(test)

###################################################
# Main School Class - Everything gets stored here #
###################################################
# class School:
#   def __init__():
#     pass
#   print("""
#     ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
#      ####### ######  ###### #      #    #     #  #    ####    #     #
#         #    #       #      # #    #    #     #  #   #    #   #     #
#         #    #       #      #  #   #    #     #  #  #         #     #
#         #    #####   #####  #   #  #    #######  #  #    ##   #######
#         #    #       #      #    # #    #     #  #  #     #   #     #
#         #    #       #      #     ##    #     #  #   #   ##   #     #
#         #    ######  ###### #      #    #     #  #    ### #   #     #
#     ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤ """)
#   def run():
#     pass

# School.run()
