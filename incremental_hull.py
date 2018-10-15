# imports
import sys
import Graphs
import matplotlib.pyplot as plt 
import time

# def
def getKey(item):
    return item.x
# endDef

# def
def incremental_Hull (pointsX, pointsY):
    points = []

    for i in range(len(pointsX)):
        point = Graphs.Point(pointsX[i], pointsY[i])
        points.append(point)

    points = sorted(points, key = getKey)



    return pointsX
# endDef

# def
def printPoints (points):
    for i in points:
        print("(%s, %s)"%(str(i.x), str(i.y)))
# endDef

# def
def point_Op(p1, p2, p3):
   x1 = p1.x - p2.x
   x2 = p1.x - p3.y
   y1 = p1.y - p2.y
   y2 = p1.y - p3.y 

   total = (y2 * x1) - (y1 * x2)

   return total
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
        (pointsX, pointsY) = Graphs.ellipticalGraph(n, a, b, r)
        print("Elipse")
    
    elif t == "r":
        (pointsX, pointsY) = Graphs.rectangularGraph(n, a, b, r)
        print("Rectangulo")
    # endIf

    """for i in range(len(pointsX)):
        print ("(%s, %s)" %(str(pointsX[i]), str(pointsY[i])))"""

    start_time = time.time()
    hull = incremental_Hull (pointsX, pointsY)
    print ("Incremental Hull gasto %s segundos"%(time.time() - start_time))

    plt.plot(pointsX, pointsY)
    plt.show()
# endIf