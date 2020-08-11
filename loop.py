import itertools

string = 'hhhhheeeellllp'

x = ''.join(c[0] for c in itertools.groupby('hhhhheeeellllp'))
print(x)
