# imports
import sys
import Graphs
import matplotlib.pyplot as plt 
import time

# def
def incremental_Hull (Points):
    print ("Incremental Hull")
    return Points
# endDef

# If
if (len(sys.argv) < 6):
    print("Faltan argumentos")
    print("Modo de uso: python incremental_hull n t a b r")

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

    # If
    if t == "e":
        distribution = Graphs.ellipticalGraph(n, a, b, r)
        print("Elipse")
        print (distribution)
    
    elif t == "r":
        distribution = Graphs.rectangularGraph(n, a, b, r)
        print("Rectangulo")
        print(distribution)
    # endIf

    start_time = time.time()
    hull = incremental_Hull (distribution)
    print ("Incremental Hull gasto %s segundos"%(time.time() - start_time))
# endIf