# https://www.hackerrank.com/contests/w4/challenges/crush
import fileinput

## Read input // O(M)
inputf = fileinput.input()
N, M = map(int, inputf.next().split())
intervals = map(lambda x: map(int, x.split()), inputf)

## Create a list of interval edges, 
## with +k at the left edges and -k at the right edges // O(M)
#edges = reduce(lambda x, y: x + y,
#               map(lambda (a, b, k): [(a, k), (b, -k)], intervals)) #SLOW!!

edges = [x for y in map(lambda (a, b, k): [(a, k), (b, -k)], intervals) for x in y]

## Sort the interval edges, breaking ties by placing left edges
## before right edges // O(M logM)
edges = sorted(edges, key = lambda (a, k): (a, -k))
## Throw away the edges at this point and keep only the steps // O(M)
steps = map(lambda (x, y): y, edges)

## Output the maximum of the cumulative sums of the list // O(M)
#print max(reduce(lambda x, y: x + [x[-1] + y], steps, [0])) #SLOW!!
cumsum = [0]
for step in steps:
    cumsum.append(cumsum[-1] + step)
print max(cumsum)


