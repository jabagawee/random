import random
from time import time

is_sorted = lambda l: all(l[i] <= l[i+1] for i in xrange(len(l)-1))

for length in xrange(1, 12):
    array = [random.randint(1, length*5) for i in xrange(length)]

    counter = 0
    t1 = time()
    while not is_sorted(array):
        counter += 1
        random.shuffle(array)
    t2 = time()

    print "length %s:\t%d iterations in %f seconds" %(length, counter, t2-t1)
