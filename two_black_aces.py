#! /usr/bin/env python

# finding the second black ace in a shuffled deck
from random import shuffle
from collections import Counter
from math import log10 as log

CASES = 100000
distribution = Counter()

for case in xrange(CASES):
    # black aces are 'a'
    deck = ['a'] * 2 + ['b'] * 50
    shuffle(deck)
    deck = ''.join(deck)
    distribution[deck.rfind('a')] += 1

for num in xrange(52):
    occurrences = distribution[num]
    num = str(num+1).zfill(2)
    dots = '.' * (occurrences / (CASES / 1000))
    print "%s: %s %s" %(num, str(occurrences).zfill(int(log(CASES))-1), dots)
