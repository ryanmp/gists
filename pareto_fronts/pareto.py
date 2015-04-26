import random

import matplotlib.pyplot as plt
import seaborn
import time, math

random.seed(123456)



# simple_cull is n^2... we should be able to do n*log(n)...
# so I'll have to try some other methods....
def simple_cull(inputPoints, dominates):
    paretoPoints = set()
    candidateRowNr = 0
    dominatedPoints = set()
    while True:
        candidateRow = inputPoints[candidateRowNr]
        inputPoints.remove(candidateRow)
        rowNr = 0
        nonDominated = True
        while len(inputPoints) != 0 and rowNr < len(inputPoints):
            row = inputPoints[rowNr]
            if dominates(candidateRow, row):
                # If it is worse on all features remove the row from the array
                inputPoints.remove(row)
                dominatedPoints.add(tuple(row))
            elif dominates(row, candidateRow):
                nonDominated = False
                dominatedPoints.add(tuple(candidateRow))
                rowNr += 1
            else:
                rowNr += 1

        if nonDominated:
            # add the non-dominated point to the Pareto frontier
            paretoPoints.add(tuple(candidateRow))

        if len(inputPoints) == 0:
            break
    return paretoPoints, dominatedPoints

def dominates(row, candidateRow):
    return sum([row[x] <= candidateRow[x] for x in range(len(row))]) == len(row)



a = 0.25
b = 2

def r():
    return 8 - (2/random.uniform(a, b))


'''


times = []
set_sizes = [1,10,100,200,300,500,1000,1500,2000,3000,4000,10000,20000]


for set_size in set_sizes:
    t0 = time.time()
    inputPoints = [[r(), r()] for i in xrange(set_size)]
    paretoPoints, dominatedPoints = simple_cull(inputPoints, dominates)
    times.append(time.time() - t0)


plt.yscale('log')
plt.xscale('log')


norm_times = [(i/times[0])+set_sizes[1] for i in times]

x0 = [1 for i in set_sizes]
x1 = [math.log(i) for i in set_sizes]
x2 = [i for i in set_sizes]
x3 = [i**2 for i in set_sizes]
x4 = [i**3 for i in set_sizes]

plt.plot(set_sizes,x0,ls='--',label='1')
plt.plot(set_sizes[1:],x1[1:],ls='--',label='log(n)')
plt.plot(set_sizes,x2,ls='--',label='n')
plt.plot(set_sizes,x3,ls='--',label='n^2')
plt.plot(set_sizes,x4,ls='--',label='n^3')

plt.plot(set_sizes[1:],norm_times[1:], marker='o', label='normalized run times')

plt.ylabel('time')
plt.xlabel('input size')

plt.gca().set_xlim(left=1)
plt.gca().set_ylim(bottom=0.01)

plt.legend()

plt.show()

'''

inputPoints = [[r(), r()] for i in xrange(3000)]
paretoPoints, dominatedPoints = simple_cull(inputPoints, dominates)

print "*"*8 + " non-dominated answers " + ("*"*8)
for p in paretoPoints:
    print p
print "*"*8 + " dominated answers " + ("*"*8)
for p in dominatedPoints:
    print p

paretoPoints = list(paretoPoints)
paretoPoints.sort()


ax = [i[0] for i in paretoPoints]
ay = [i[1] for i in paretoPoints]

bx = [i[0] for i in dominatedPoints]
by = [i[1] for i in dominatedPoints]

seaborn.set()
current_palette = seaborn.color_palette()

plt.scatter(bx, by, c=current_palette[0])
plt.plot(ax, ay, c=current_palette[2], linestyle='--')
plt.scatter(ax, ay, c=current_palette[2])

plt.show()
