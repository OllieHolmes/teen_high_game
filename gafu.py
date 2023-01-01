from names import boys_names, girls_names, surnames
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
