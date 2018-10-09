import sys

def getKey(item):
    return item[0]

def jarvis_Aux ():



N = [
    (3, 2),
    (5, 3),
    (2, 10),
    (10, 3),
    (1, 5)
]

N = sorted(N, key = getKey)
print (N)

n = sys.argv[1]
t = sys.argv[2]
a = sys.argv[3]
b = sys.argv[4]
r = sys.argv[5]

n = int(n)
a = int(a)
b = int(b)
n = int(r)

jarvis_Aux()
