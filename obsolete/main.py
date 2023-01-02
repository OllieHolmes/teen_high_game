import re
from all_names import all_names_lst
from last_names import surnames
# text = open('.txt', 'r').read()
# reg_text = re.findall('[A-Z][A-Z]+', text)
#
# print(reg_text)

# boys_names = []
# girls_names = []
#
# counter = 0
# for name in all_names_lst:
#     if counter % 2 == 0:
#         boys_names.append(name)
#     else:
#         girls_names.append(name)
#     counter += 1
#
# print(boys_names)
# print(girls_names)

surnames_title = [name.title() for name in surnames]
surnames_title.sort()
print(surnames_title)