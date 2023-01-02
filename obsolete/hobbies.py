import re
from nltk import word_tokenize

text = open('hobbies.txt', encoding='utf8').read()
h3_lst = re.findall('<h3.*</h3>', text)
h3_text = ""
for i in h3_lst:
    h3_text += i + ", "
headers = re.findall('[A-Z]\w+ ?\w* ?\w* ?\w* ?\w* ?\w* ?\w* ?\w* ?[a-z]+', h3_text)
raw_reg_text = re.findall('<ul.+</ul>', text)
raw_reg_join = ""
for i in raw_reg_text:
    raw_reg_join += i + ", "
li_items_reg_text = re.findall('<li.+[A-Z]\w*.*</li>', raw_reg_join)

new_join = ""
for i in li_items_reg_text:
    new_join += i + ", "

clean_list = re.sub(r'(</?li>|</?ul>)', " ", new_join)
tokenized_clean_list = re.findall("[A-Z][a-z]+ ?[a-z]* ?[a-z]* ?[a-z]* ?[a-z]*", clean_list)

# print(tokenized_clean_list)
from structured_hobby_list import list_of_hobbies

for i in list_of_hobbies:
    print(i)