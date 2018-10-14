# imports
import random
import math

# Inicio clase para representar puntos
class Point:
    # def
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    # endDef

    # def
    def __str__ (self):
        return "[%s, %s]"%(self.x, self.y)
    # endDef
#Fin clase punto

# Inicio de Graficación

# Gráfica rectangular
# def
def rectangularGraph (n, a, b, r):
    pointCant = 0
    points = []

    #while
    while pointCant < n:
        x = random.uniform(1, a)
        y = random.uniform(1, b)
        
        rotY = (x*math.sin(r)) + (y*math.cos(r))
        rotX = (x*math.cos(r)) - (y*math.sin(r))

        punto = Point(rotX, rotY)

        points.append(punto)

        pointCant = len(points)
    # endWhile

    return points
# endDef

# Gráfica elíptica
# def
def ellipticalGraph (n, a, b, r):
    pointCant = 0
    points = []

    # while
    while pointCant < n:
        theta = 0

        value = random.random() / 4
        thetaValue = math.atan(b/a * math.tan(2*3.14*value))

        secondValue = random.random()

        # If
        if secondValue < 0.25:
            theta = thetaValue

        elif secondValue < 0.5:
            theta = 3.14 - thetaValue

        elif secondValue < 0.75:
            theta = 3.14 + thetaValue
        
        else:
            theta = -thetaValue
        # endIf 
        radius = a*b / math.sqrt((b*math.cos(theta))**2 + (a*math.sin(theta))**2)
        rradius = radius * math.sqrt(random.random())

        x = rradius * math.cos(r)
        y = rradius * math.sin(r)

        rotY = (x * math.sin(r)) + (y * math.cos(r))
        rotX = (x * math.cos(r)) - (y * math.sin(r))

        point = Point(rotX, rotY)

        points.append(point)
        pointCant = len(points)
    # endWhile
    return points
# endDef