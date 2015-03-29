# https://www.hackerrank.com/challenges/icecream-parlor
import fileinput
inputf = fileinput.input()

#with open("/Users/ste/Desktop/input01.txt") as inputf:
#    T = int(inputf.next())
#    tests, Ms = [], []
#    for _ in range(T):
#        M = int(inputf.next())
#        N = int(inputf.next())
#        test = map(int, inputf.next().split())
#        tests.append(test)
#        Ms.append(M)

T = int(inputf.next())
tests, Ms = [], []
for _ in range(T):
    M = int(inputf.next())
    N = int(inputf.next())
    test = map(int, inputf.next().split())
    tests.append(test)
    Ms.append(M)

#xs = [1, 4, 5, 3, 2]
#xs = [2, 2, 4, 3]
#idxs = {xs[i]: i for i in range(len(xs))}
#M = 4
def get_pair(xs, M):
    costs = {}
    for flavour, cost in enumerate(xs):
        costs[cost] = costs.get(cost, []) + [flavour]
    for cost, flavours in costs.iteritems():
        if M == 2*cost and len(flavours) > 1:
            return flavours[0]+1, flavours[1]+1
        if M-cost in costs:
            return flavours[0]+1, costs[M-cost][0]+1
    return None

for test, M in zip(tests, Ms):
    i, j = sorted(get_pair(test, M))
    print i, j