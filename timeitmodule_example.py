import timeit

##print timeit.timeit('1+3', number=50000000)

##input_list = range(100)
##
##def div_by_five(num):
##    return num % 5 == 0
##
##xyz = (i for i in input_list if div_by_five(i)) #generator of #s
##
##for i in xyz:
##    print i

##xyz = [i for i in input_list if div_by_five(i)]


print timeit.timeit('''input_list = range(100)

def div_by_five(num):
    return num % 5 == 0

xyz = (i for i in input_list if div_by_five(i)) #generator of #s

for i in xyz:
    x= i''', number=500000) #compare this generator to list
