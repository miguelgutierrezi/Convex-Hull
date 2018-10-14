# imports
import sys

# If
if (len(sys.argv) < 6):
    print("Faltan argumentos")
    print("Modo de uso: python dc_hull n t a b r")

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

# endIf