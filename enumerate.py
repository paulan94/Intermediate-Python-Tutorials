#enum sentdex intermediate python programming p 7

example = ['left', 'right', 'up', 'down']

##for i in range(len(example)): #usually not good to use range len, use enum instead
##    print (i, example[i])

for i,j in enumerate(example):
    print i,j

new_dict = dict(enumerate(example))

print new_dict

##[print(i,j) for i,j in enumerate(new_dict)] #works in python 3


