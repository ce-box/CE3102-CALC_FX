import numpy as np
import sys
from sympy import *

def biseccion(func,rango, tol, iterMax):
    
    #Funcion de prueba: "E**x - x - 2"

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy 
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)

    cont = 0 #Se inicializa el contador

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    while(cont <= iterMax):
        
        x = (rango[0] + rango[1]) / 2 #Calcula punto medio
        y = fx(x) #Se calcula el valor de f(x)
        
        if(fx(rango[0])*y < 0):
            rango[1] = x
            
        if(y*fx(rango[1]) < 0):
            rango[0] = x

        if(np.absolute(y) < tol):
            break

        cont += 1 #Incrementa contador

    return [x, np.absolute(y), cont] #Retorna la aproximación del cero de f(x), el error, y la cantidad de iteraciones

def newton_raphson(func, xk, tol, iterMax):

    #Funcion de prueba: "cos(2*x)**2 - x**2"

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy
    df = f.diff(x) #Se calcula la derivada de "f"
    
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)
    dfx = lambdify(x, df, modules=['numpy']) #Se inicializa la derivada de la función f(x)

    cont = 0 #Se inicializa el contador

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    while(cont < iterMax):

        xk = xk - ((fx(xk))/(dfx(xk)))
        y = fx(xk)

        if(np.absolute(y) < tol):
            break

        cont += 1 #Incrementa contador

    return [xk, np.absolute(y), cont] #Retorna la aproximación del cero de la función, el error, y la cantidad de iteraciones
        

def secante(func, x0, x1, tol, iterMax):

    #Función de prueba: "cos(2*x)**2 - x**2"

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy 
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)

    cont = 0 #Se inicializa el contador
    errores = [] #Se crea una lista de los errores calculados para graficar

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    while(cont <= iterMax):

        xk = x1 - ((x1-x0)/(fx(x1)-fx(x0)))*fx(x1) #Se calcula xk
        error = np.absolute(fx(xk)) #Se calcula el error
        errores.append(error) #Se añade el error a la lista de errores

        if(error < tol):
            break

        x0 = x1 #Reasigna x0
        x1 = xk #Reasigna x1

        cont += 1 #Incrementa contador

    return [xk, cont, np.absolute(fx(xk))] #Retorna xk, las iteraciones, y f(x)
