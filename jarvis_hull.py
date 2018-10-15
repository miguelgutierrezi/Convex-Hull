# imports
import sys
import Graphs
import matplotlib.pyplot as plt
import math
import time

# def
def point_Op(p1, p2, p3):
    val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

    # If
    if val == 0:
        return 0
    
    elif val > 0:
        return 1
    
    else:
        return 2
    # endDef
# endDef

# def
def compare (x1, x2, y1, y2):
    a = (y1*y1) + (x1*x1)
    b = (y2*y2) + (x2*x2)

    # If
    if a == b:
        return 0
    
    elif a < b:
        return -1
    
    else:
        return 1
    # endIf
# endDef

# def
def distance(p1, p2, p3):
    x1 = p1.x - p2.x
    x2 = p1.x - p3.x
    y1 = p1.y - p2.y
    y2 = p1.y - p3.y

    return compare(x1, x2, y1, y2)
# endDef

# def
def points_Distance(p1, p2):
    d = math.sqrt(((p2.x-p1.x)*(p2.x-p1.x)) + ((p2.y-p1.y)*(p2.y-p1.y)))
    return d
# endDef

# def
def getKey(item):
    return item.y
# endDef

# def
def jarvis_Hull (pointsX, pointsY):
    points = []

    # for
    for i in range(len(pointsX)):
        point = Graphs.Point(pointsX[i], pointsY[i])
        points.append(point)
    # endFor

    # If
    if len(points) < 3:
        return
    # endIf

    hull = []

    left = 0

    # for
    for i in range (1, len(points)):
        # If
        if points[i].x < points[left].x:
            left = i
        # endIf
    # endFor

    start = left

    # while
    while True:
        hull.append(points[start])

        q = (start + 1) % len(points)
        # for
        for i in range (len(points)):
            # If
            if (point_Op(points[start], points[i], points[q]) == 2):
                q = i
            # endIf
        # endFor
        start = q
        
        # If
        if (start == left):
            break
        # endIf
    # endWhile

    return hull

# endDef

# def
def printPoints (points):
    for i in points:
        print("(%s, %s)"%(str(i.x), str(i.y)))
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
    hull = jarvis_Hull (pointsX, pointsY)
    print ("Jarvis Hull gasto %s segundos"%(time.time() - start_time))

    printPoints(hull)

    hull.append(hull[0])
    
    x = []
    y = []

    for p in hull:
        x.append(p.x)
        y.append(p.y)

    plt.scatter(pointsX, pointsY)
    plt.plot(x, y, color='g')
    plt.show()
# endIf