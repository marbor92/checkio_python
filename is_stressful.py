import re

string = 'I need HHHHHEEEELLLLP'
red_words = ['help', 'urgent', 'asap', 'asp']

# # all letters uppercase
# if string.isupper():
#      print(True)

# checking if red words are included
remover = re.sub(r'\W+', ' ', string)
words = remover.lower()





#
# # at least 3 !
# if string[-3:] == "!!!":
#     print(True)

# different marks between red words' letters