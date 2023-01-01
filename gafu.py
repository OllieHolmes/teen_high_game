from names import boys_names, girls_names, surnames
from hobbies import hobby_list
from random import randint

# ----- Name Generator -----
def generate_name(xx=False):
    rand_last = randint(0, len(surnames)-1)
    new_name = None
    if xx == False:
      rand_first = randint(0, len(girls_names)-1)
      new_name = (surnames[rand_last], girls_names[rand_first])
    else:
      rand_first = randint(0, len(boys_names)-1)
      new_name = (surnames[rand_last], boys_names[rand_first])
    return new_name

# ----- Hobby Generator -----
def assign_npc_hobbies(hobby_type):
    npc_hobbies = {}
    num_of_hobbies = randint(1,3)
    hobby_num = randint(0, len(hobby_list[hobby_type]-1))
    npc_hobbies["main"] = hobby_list[hobby_type][hobby_num]
    for n in range(num_of_hobbies):
        hobby_cat = randint(0, len(hobby_list)-1)
        hobby_num = randint(0, len(hobby_list[hobby_cat])-1)
        npc_hobbies["secondary"] = hobby_list[hobby_cat][hobby_num]