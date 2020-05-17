# -*- coding: utf-8 -*-
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
D = 100  #Numero de dimensiones (20 - 50 - 100)

# Elije alguna de estas funciones: sphere - schwefel - rastrigin -griewank

function=rastrigin

if((function == sphere) or function == schwefel): #Establezco limites de cada una de las funciones
    LS = 100
    LI = -100
if(function==rastrigin):
    LS = 5.12
    LI = -5.12
if(function==griewank):
    LS = 600
    LI = -600

count=0
tw=[0.2,0.6,1.0] #Tweak
n=[10,20] #Numero de vecinos
p=[1.0,2.0,3.0] #Valor perturbación

cuenta=0
def contador(): #función que contara los NMFO
  global cuenta
  cuenta+=1

for i in range(0,len(tw)):
    for j in range(0,len(n)):     
        for z in range(0,len(p)):
            MB=[np.zeros(E)]
            ttbest=[np.zeros(5000)]
            for k in range(0,E):
               S = [np.zeros(D)]
               R = [np.zeros(D)]
               for l in range(0,D):
                   S[0][l] = random.uniform(LI, LS)
               H = S
               fh=function(H)
               Best=S
               fbest=function(Best)
               
               ccount=0
               cuenta=0
               while(cuenta<5000):
                   while (count < n[j] ):
                       for m in range(0, D):
                           R[0][m] = float(S[0][m]) + random.uniform(0-tw[i],0+tw[i])
                       if(cuenta>=5000):
                               break
                       fr=function(R)
                       contador()
                       fs=function(S)
                       if(fr.Result < fs.Result) :
                           if(cuenta>=5000):
                               break
                           S=R
                           fs=function(S)
                           contador()
                       count+=1
                   if(fs.Result < fbest.Result):
                       if(cuenta>=5000):
                               break
                       Best=S
                       fbest=function(Best)
                       contador()
                   if (fs.Result < fh.Result):
                       if(cuenta>=5000):
                               break
                       H=S
                       fh=function(H)
                       contador()
                   for q in range(0,D):
                       S[0][q] = float(H[0][q]) + random.uniform(0-p[z],0+p[z])
                   if(cuenta>=5000):
                               break
                   fs=function(S)
                   contador()
                   ttbest[0][ccount]=fbest.Result
                   ccount+=1
                   count=0
               MB[0][k]=np.mean(ttbest)
            print(tw[i],n[j],p[z],np.mean(MB))

