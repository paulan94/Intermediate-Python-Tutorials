#the GIL (Global Interpreter Lock)
#Tutorial 10: Multiprocessing

import multiprocessing

def spawn(num,num2):
    print 'Spawned! {} {}'.format(num,num2)


if __name__ == "__main__":
    for i in range(5000):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start() #starts process
##        p.join() #wait for process to complete
