#https://www.hackerrank.com/challenges/jim-and-the-skyscrapers
import fileinput

def count_paths(hs):
    visible, paths = [], 0
    for h in hs:
        while visible and visible[-1][0] < h:
            visible.pop()
        if visible and visible[-1][0] == h:
            paths += visible[-1][1]
            visible[-1][1] += 1
        else:
            visible.append([h, 1])
    return paths*2

inputf = fileinput.input()
N = int(inputf.next())
hs = map(int, inputf.next().split())
print count_paths(hs)