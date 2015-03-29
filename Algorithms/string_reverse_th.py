def characterReverse(s):
    ## Convert string to array -- to support item assignment
    a = list(s)
    ## Traverse the array
    i, n = 0, len(a)
    while i < n:
        ## Skip all non-'t' chars: they are already in the
        ## right place
        while i < n and a[i] != 't':
            i += 1
        ## Once you find a 't', traverse a whole block of 't'
        ## and 'h' characters. Record the length of the block
        ## and the number of 'h's it contains
        k, hs = 0, 0
        while i+k < n and a[i+k] in ['t', 'h']:
            if a[i+k] == 'h':
                hs += 1
            k += 1
        ## Process the block: all the 'h's go at the front.
        a[i:(i+k)] = ['h']*hs + ['t']*(k-hs)
        ## Keep going
        i += k
    return "".join(a)


with open("input003.txt") as f:
    s = f.read()
print characterReverse(s)
with open("output003.txt") as f:
    print f.read()