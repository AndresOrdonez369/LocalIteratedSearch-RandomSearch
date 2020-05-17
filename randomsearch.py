"""


@author: andres
"""
import numpy as np
import random
import math

class sphere:
    def __init__(self, vec):
        Aux = 0
        
        for i in range(0,D):
            vector = float(vec[0][i])
            Aux = Aux + vector**2
        self.Result = Aux

class schwefel:
     def __init__(self, vec):
        Aux = 0
        Aux0 = 0
        for i in range(0,D):
            Aux = 0
            for j in range(0,(i+1)):
                Aux += vec[0][j]
            Aux0 += Aux**2    
        self.Result = Aux0
        
class griewank:
    def __init__(self, vec):
        Aux0 = 0
        Aux1 = 1
        for i in range(0,D):
            vector = float(vec[0][i])
            Aux0 = Aux0 + vector**2
            Aux1 = Aux1 * math.cos(vector/math.sqrt(i+1))
        Aux = Aux0/4000 - Aux1 + 1
        self.Result = Aux 


class rastrigin:
    def __init__(self, vec):
        Aux = 0   
        for i in range(0,D):
            vector = float(vec[0][i])
            Aux += (vector**2 - (10 * math.cos(2*math.pi*vector)) + 10)
        self.Result = Aux


E=30 #Numero de ejecuciones
D = 20 #Numero de dimensiones (20 - 50 - 100)

# Elije alguna de estas funciones: sphere - schwefel - rastrigin -griewank

function=sphere

if((function == sphere) or function == schwefel):
    LS = 100
    LI = -100
if(function==rastrigin):
    LS = 5.12
    LI = -5.12
if(function==griewank):
    LS = 600
    LI = -600

count=0
cuenta=0
def contador(): 
  global cuenta
  cuenta+=1

MB=[np.zeros(E)]
for k in range(0,E):
    S = [np.zeros(D)]
    for l in range(0,D):
        S[0][l] = random.uniform(LI, LS)
    fs=sphere(S)
    Best=S
    fbest=sphere(Best)
    cuenta=0
    while(cuenta<5000):
        for l in range(0,D):
            S[0][l] = random.uniform(LI, LS)
        if(cuenta>=5000):
            break
        fs=function(S)
        contador()
        if(fs.Result < fbest.Result) :
            if(cuenta>=5000):
                break
            Best=S
            fbest=function(Best)
            contador()
    MB[0][k]=fbest.Result
#               
print(np.mean(MB))  # imprime el promedio de los resultados encontrados en las 7 ejecuciones


