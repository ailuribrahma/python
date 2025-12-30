import itertools
c = ['BRAHMA','REDDY','NANI']
cycle = itertools.cycle(c)
for i in range(10):
    print(next(cycle))