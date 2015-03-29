## https://www.hackerrank.com/challenges/candies

import fileinput
inputf = fileinput.input()
N = int(inputf.next())
rates = map(int, inputf)

candies = [1] * N
for i in range(1, N):
    if rates[i] > rates[i-1]:
        candies[i] = candies[i-1]+1
for i in range(N-1, 0, -1):
    if rates[i-1] > rates[i]:
        candies[i-1] = max(candies[i-1], candies[i]+1)
print sum(candies)
