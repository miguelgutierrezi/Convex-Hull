#!/usr/bin/python

##################################################
#     Taller 4: Algoritmo Divide and Conquer     #
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
import os

#-------------------------------------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------------------------------------
# def
def farthest_Point(s, e, points):
    maximum = -math.inf

    # for
    for p in points:
		# If
        if p != s and p != e:
            dist = distance(s, e, p)
			# If
            if dist > maximum:
                maximum = dist
                maxP = p
            # endIf
        # endIf
    # endFor
    
    # If
    if maximum != -math.inf:
        return maxP
    else:
        return None
    # endIf
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def distance(start, end, point): 
	nom = abs((end.y - start.y) * point.x - (end.x - start.x) * point.y + end.x * start.y - end.y * start.x)
	denom = ((end.y - start.y)**2 + (end.x - start.x) ** 2) ** 0.5
	result = nom / denom
	return result
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def left_Points (s, e, points):
    left = []
     
    # for
    for p in points:
        # If
        if point_Op(s, e, p) == 2:
            left.append(p)
        # endId
    # endFor
    return left
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def right_Points (s, e, points):
    right = []

    # for
    for p in points:
        # If
        if point_Op(s, e, p) == 1:
            right.append(p)
        # endId
    # endFor
    return right
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def extreme_Points(points):
    minimum = math.inf
    maximum = -math.inf
    posMax = 0
    posMin = 0

    # def
    for i in range(len(points)):
        # for
        if points[i].y > maximum:
            maximum = points[i].y
            posMax = i
        # endIf

        # If
        if points[i].y < minimum:
            minimum = points[i].y
            posMin = i
        # endIf
    # endFor
    return (points[posMin], points[posMax])
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def sub_Hull (a, b, S):
    S = left_Points(a, b, S)
    c = farthest_Point(a, b, S)
    # If
    if c == None:
        return [b]
    # endIf

    hull = sub_Hull(a, c, S)
    hull = hull + (sub_Hull(c, b, S))

    return hull 
# endDef

#-------------------------------------------------------------------------------------------------------------
# def
def DC_Hull (points):
    (minimum, maximum) = extreme_Points(points)

    hull = sub_Hull(minimum, maximum, points)
    hull = hull + (sub_Hull(maximum, minimum, points))

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

    file = open("salida_dc.txt", "w")
    for tam in range (100, 100000, 100):
        start_time = time.time()
        hull = DC_Hull (points)
        final_time = time.time() - start_time
        file.write("%d,%f\n"%(tam, final_time))
    file.close()

    start_time = time.time()
    hull = DC_Hull (points)
    print ("Divide and Conquer Hull gasto %s segundos"%(time.time() - start_time))

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
