# https://www.hackerrank.com/challenges/picking-cards
import fileinput

inputf = fileinput.input()
T = int(inputf.next())
Ns, tests = [], []
for _ in range(T):
    Ns.append(int(inputf.next()))
    tests.append(map(int, inputf.next().split()))

def ways(cs, N):
    counts = {i: 0 for i in range(N+1)}
    for c in cs:
        counts[c] += 1
    leq_than, current = {}, 0
    for i in range(N):
        current += counts[i]
        leq_than[i] = current
    res = leq_than[0]
    for i in range(1, N):
        res = res * (leq_than[i]-i) % 1000000007
    return res

for test, N in zip(tests, Ns):
    print ways(test, N)
