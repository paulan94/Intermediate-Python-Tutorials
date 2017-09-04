
##xyz = [i for i in range(5000000)] #list takes longer because its stored into memory
##print 'done'
##xyz = (i for i in range(5000000)) #generator doesnt store as list or into memory
##print 'done' #this is almost instant after list is created

input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    return num % 5 == 0

xyz = (i for i in input_list if div_by_five(i)) #return #s that are div by 5
for i in xyz:
    print i

##[print(i) for i in xyz] python 3 only

xyz = [i for i in input_list if div_by_five(i)] #cool
##print xyz

#these were never in memory, would run out of memory with lists
#lists take a lot of memory, generators might run out of time

##xyz = ( ( (i,ii) for ii in range(50000000))for i in range(5))
##for i in xyz:
##    for ii in i:
##        print ii
        

#python 3 this would work
##xyz = (print(i) for i in range(5))
##for i in xyz:
##    i
