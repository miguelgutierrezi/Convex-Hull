# imports
import random
import math

# Inicio Clase Punto
# Class
class Point:
    # def
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    # endDef
# endClass
# Fin Clase punto

# Inicio de Graficación

# Gráfica rectangular
# def
def rectangularGraph (n, a, b, r):
    pointCant = 0
    pointsX = []
    pointsY = []

    #while
    while pointCant < n:
        x = random.uniform(1, a)
        y = random.uniform(1, b)
        
        rotY = (x*math.sin(r)) + (y*math.cos(r))
        rotX = (x*math.cos(r)) - (y*math.sin(r))

        pointsX.append(rotX)
        pointsY.append(rotY)

        pointCant = len(pointsX)
    # endWhile

    return (pointsX, pointsY)
# endDef

# Gráfica elíptica
# def
def ellipticalGraph (n, a, b, r):
    pointCant = 0
    pointsX = []
    pointsY = []

    # while
    while pointCant < n:
        value = random.random() / 4
        thetaValue = math.atan(b/a * math.tan(2*math.pi*value))

        secondValue = random.random()

        # If
        if secondValue < 0.25:
            theta = thetaValue

        elif secondValue < 0.5:
            theta = math.pi - thetaValue

        elif secondValue < 0.75:
            theta = math.pi + thetaValue
        
        else:
            theta = -thetaValue
        # endIf 
        radius = a*b / math.sqrt((b*math.cos(theta))**2 + (a*math.sin(theta))**2)
        rradius = radius * math.sqrt(random.random())

        x = rradius * math.cos(theta)
        y = rradius * math.sin(theta)

        rotY = (x * math.sin(r)) + (y * math.cos(r))
        rotX = (x * math.cos(r)) - (y * math.sin(r))

        pointsX.append(rotX)
        pointsY.append(rotY)
        pointCant = len(pointsX)
    # endWhile
    return (pointsX, pointsY)
# endDef