# imports
import sys

# def
def getKey(item):
    return item[0]
# endDef

# def
def jarvis_Aux ():
    print ("Hola")
# endDef

N = [
    (3, 2),
    (5, 3),
    (2, 10),
    (10, 3),
    (1, 5)
]

N = sorted(N, key = getKey)
print (N)

# If
if (len(sys.argv) < 6):
    print("Faltan argumentos")
    print("Modo de uso: python jarvis_hull n t a b r")

else:
    n = sys.argv[1]
    t = sys.argv[2]
    a = sys.argv[3]
    b = sys.argv[4]
    r = sys.argv[5]

    n = int(n)
    a = int(a)
    b = int(b)
    r = int(r)

    jarvis_Aux()
# endIf