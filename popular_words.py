# Function checks the popularity of certain words in the text.


text = "When I was One " \
       "I had just begun " \
       "When I was Two " \
       "I was nearly new "

words = ['i', 'was', 'three', 'near']


def popular_words(text, words):
    pos = 0
    new_list = text.lower().split()
    this_dict = {}
    for n in words:
        counted_word = new_list.count(words[pos])
        this_dict[words[pos]] = counted_word
        pos += 1
    return this_dict

