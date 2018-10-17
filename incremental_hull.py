#!/usr/bin/python

##################################################
#         Taller 4: Algoritmo Incremental        #
#              para Cascos Convexos              #
# Miguel Ángel Gutiérrez - Juan Sebastián Bastos #
# Análisis de Algoritmos                         #
# Pontificia Universidad Javeriana               #
##################################################

# imports
import sys
import Graphs
# import matplotlib.pyplot as plt
import math
import time

#-------------------------------------------------------------------------------------------------------------
# def
def points_rightTurn(p1, p2, p3):
    x1 = p1.x - p2.x
    x2 = p1.x - p3.x
    y1 = p1.y - p2.y
    y2 = p1.y - p3.y

    total = y2 * x1 - y1 * x2

    return total
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def getKey(item):
    return item.y
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def incremental_Hull (points):
    points = sorted(points, key = getKey)

    Lupper = []
    Lupper.append(points[0])
    Lupper.append(points[1])

    # for
    for i in range (2, len(points)):
        Lupper.append(points[i])
        # while
        while len(Lupper) > 2 and points_rightTurn(Lupper[len(Lupper)-3], Lupper[len(Lupper)-2], Lupper[len(Lupper)-1]) >= 0:
           Lupper.pop(len(Lupper)-2)
        # endWhile
    # endFor

    Llower = []
    Llower.append(points[len(points)-1])
    Llower.append(points[len(points)-2])

    # for
    for i in range (len(points) - 3, -1, -1):
        Llower.append(points[i])
        # while
        while len(Llower) > 2 and points_rightTurn(Llower[len(Llower)-3], Llower[len(Llower)-2], Llower[len(Llower)-1]) >= 0:
           Llower.pop(len(Llower)-2)
        # endWhile
    # endFor

    Llower.pop(0)
    Llower.pop(len(Llower) - 1)

    hull = Llower + Lupper
    
    return hull
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def printPoints (points):
    for i in points:
        print("(%s, %s)"%(str(i.x), str(i.y)))
# endDef

#-------------------------------------------------------------------------------------------------------------
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

    # If
    if t == "e":
        (pointsX, pointsY) = Graphs.ellipticalGraph(n, a, b, r)
        print("Elipse")
    
    elif t == "r":
        (pointsX, pointsY) = Graphs.rectangularGraph(n, a, b, r)
        print("Rectangulo")
    # endIf

    points = []

    # for
    for i in range(len(pointsX)):
        point = Graphs.Point(pointsX[i], pointsY[i])
        points.append(point)
    # endFor

    file = open("salida_incremental.txt", "w")
    for tam in range (100, 100000, 100):
        start_time = time.time()
        hull = incremental_Hull (points)
        final_time = time.time() - start_time
        file.write("%d %f\n"%(tam, final_time))
    file.close()

    start_time = time.time()
    hull = incremental_Hull (points)
    print ("Incremental Hull gasto %s segundos"%(time.time() - start_time))
    
    printPoints(hull)

    hull.append(hull[0])
    
    """x = []
    y = []

    for p in hull:
        x.append(p.x)
        y.append(p.y)

    plt.scatter(pointsX, pointsY, facecolor="black")
    plt.scatter(x, y, facecolor="green")
    plt.plot(x, y, color='g')
    plt.show()"""
# endIf
