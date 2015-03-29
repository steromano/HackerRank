## https://www.hackerrank.com/challenges/red-john-is-back
import fileinput
inputf = fileinput.input()
T = int(inputf.next())
Ns = map(int, inputf)

maxN = max(Ns)

## A configuration starts either with an horizontal or a vertical brick
nconfs = [1, 1, 1, 1]
while len(nconfs) <= maxN:
    nconfs.append(nconfs[-1] + nconfs[-4])

def sieve(M):
    s = range(M+1)
    s[1] = 0
    for i in range(M+1):
        if s[i] == 0:
            continue
        k = 2
        while i*k < M+1:
            s[i*k] = 0
            k += 1
    return s

def nprimes(M, sieve):
    return sum(p != 0 for p in sieve if p <= M)
    
s = sieve(nconfs[-1])
for N in Ns:
    print nprimes(nconfs[N], s)

    
    

