#https://www.hackerrank.com/contests/hour-of-code2013/challenges/longest-increasing-subsequent

## UNSOLVED!
import fileinput
def max_increasing_subsequence(xs, n):
    a = [0] * n
    b = []
    for j in range(n):
        if j % 100 == 0:
            print j
        for i in range(n):
            if xs[j] > xs[i]:
                b.append(a[i])
            else:
                b.append(max(a[i], a[j]+1))
        a, b = b, []
    return max(a)
    

#xs = [29471,5242,21175,28931,2889,7275,19159,21773,1325,6901]
#xs = [2,7,4,3,8]
#with open("/Users/ste/Desktop/input09.txt") as f:
#    n = int(f.next())
#    xs = [int(x) for x in f]

inputf = fileinput.input()
n = inputf.next()
xs = map(int, inputf)

print max_increasing_subsequence(xs, n)