##def simple_gen():
##    yield 'oh'
##    yield 'hello'
##    yield 'there'
##
##x = [i for i in simple_gen()]
##print x
##

import timeit

CORRECT_COMBO = (3,6,1)

##found_combo = False
##for c1 in range(10):
##    if found_combo:
##        break
##    for c2 in range(10):
##        if found_combo:
##            break
##        for c3 in range(10):
##            if (c1,c2,c3) == CORRECT_COMBO:
####                print 'Found the combo: {}'.format((c1,c2,c3))
##                found_combo = True
##                break
####            print (c1,c2,c3)

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1,c2,c3)

for (c1,c2,c3) in combo_gen():
    if (c1,c2,c3) == CORRECT_COMBO:
        print 'Found the combo: {}'.format((c1,c2,c3))
        break

##print timeit.timeit('''CORRECT_COMBO = (3,6,1)
##
##found_combo = False
##for c1 in range(10):
##    if found_combo:
##        break
##    for c2 in range(10):
##        if found_combo:
##            break
##        for c3 in range(10):
##            if (c1,c2,c3) == CORRECT_COMBO:
####                print 'Found the combo: {}'.format((c1,c2,c3))
##                found_combo = True
##                break''', number=5000)
