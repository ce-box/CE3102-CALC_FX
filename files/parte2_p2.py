import numpy as np
import sys
from sympy import *
from matplotlib import pyplot as plt

def biseccion(func,rango, tol, iterMax):
    
    #Funcion de prueba: "E**x - x - 2", [0,2], 10**(-10), 100

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy 
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)

    D = [] #Datos eje x (Iteraciones)
    A = [] #Datos eje y (Errores)

    cont = 1 #Se inicializa el contador

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    #Verifica que se cumpla con el teorema de Bolzano
    if(not(bolzano(fx(rango[0]),fx(rango[1])))):
        return print("No cumple con el teorema de Bolzano")

    while(cont <= iterMax):
        
        x = (rango[0] + rango[1]) / 2 #Calcula punto medio
        y = fx(x) #Se calcula el valor de f(x)

        D.append(cont)
        A.append(y)
        
        if(fx(rango[0])*y < 0):
            rango[1] = x
            
        elif(y*fx(rango[1]) < 0):
            rango[0] = x

        cont += 1 #Incrementa contador

        if(np.absolute(y) < tol):
            break

    return [x, np.absolute(y), cont, D, A] #Retorna la aproximación del cero de f(x), el error, y la cantidad de iteraciones

def falsa_posicion(func, rango, tol, iterMax):

    #Funcion de prueba: "E**x - x - 2", [0,2], 10**(-10), 100

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy 
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)

    cont = 0 #Se inicializa el contador

    D = [] #Datos eje x (Iteraciones)
    A = [] #Datos eje y (Errores)

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    #Verifica que se cumpla con el teorema de Bolzano
    if(not(bolzano(fx(rango[0]),fx(rango[1])))):
        return print("No cumple con el teorema de Bolzano")

    b = rango[0]
    a = rango[1]
    
    xk = a - ((a-b)/(fx(a)-fx(b)))*fx(a)

    D.append(cont)
    A.append(fx(xk))

    while(cont < iterMax):

        if(bolzano(fx(a),fx(xk))):
            if((fx(xk)-fx(a)) == 0): #Indefinición de denominador
                break
            b = xk
            xk = xk - ((xk-a)/(fx(xk)-fx(a))*fx(xk))
        elif(bolzano(fx(xk),fx(b))):
            if((fx(xk)-fx(b)) == 0): #Indefinición de denominador
                break
            a = xk
            xk = xk - ((xk-b)/(fx(xk)-fx(b))*fx(xk))

        D.append(cont)
        A.append(fx(xk))

        cont += 1 #Incrementa contador

        if(np.absolute(fx(xk)) < tol):
            break

    return [xk, np.absolute(fx(xk)), cont, D, A]
    
 
def newton_raphson(func, xk, tol, iterMax):

    #Funcion de prueba: "cos(2*x)**2 - x**2", 3/4, 10**(-10), 100

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy
    df = f.diff(x) #Se calcula la derivada de "f"
    
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)
    dfx = lambdify(x, df, modules=['numpy']) #Se inicializa la derivada de la función f(x)

    D = [] #Datos eje x (Iteraciones)
    A = [] #Datos eje y (Errores)

    cont = 1 #Se inicializa el contador

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    while(cont <= iterMax):

        if(dfx(xk) == 0): #Indefinición de denominador
            break

        xk = xk - ((fx(xk))/(dfx(xk)))
        y = fx(xk)

        D.append(cont)
        A.append(y)

        if(np.absolute(y) < tol):
            break

        cont += 1 #Incrementa contador

    return [xk, np.absolute(y), cont, D, A] #Retorna la aproximación del cero de la función, el error, y la cantidad de iteraciones
        

def secante(func, x0, x1, tol, iterMax):

    #Función de prueba: "cos(2*x)**2 - x**2", 3/4, 1/2, 10**(-10), 100

    x = Symbol('x') #Inicializa "x" como símbolo
    f = sympify(func) #Se traduce el string "func" a una función de sympy 
    fx = lambdify(x, f, modules=['numpy']) #Se inicializa la función f(x)

    cont = 1 #Se inicializa el contador

    D = [] #Datos eje x (Iteraciones)
    A = [] #Datos eje y (Errores)

    #Verifica que la tolerancia no sea negativa
    if (tol < 0):
        return print("La tolerancia debe ser mayor que cero")

    while(cont <= iterMax):

        if((fx(x1)-fx(x0)) == 0): #Indefinición de denominador
            break

        xk = x1 - ((x1-x0)/(fx(x1)-fx(x0)))*fx(x1) #Se calcula xk
        error = np.absolute(fx(xk)) #Se calcula el error

        D.append(cont)
        A.append(error) #Se añade el error a la lista de errores

        if(error < tol):
            break

        x0 = x1 #Reasigna x0
        x1 = xk #Reasigna x1

        cont += 1 #Incrementa contador

    return [xk, np.absolute(fx(xk)), cont, D, A] #Retorna xk, las iteraciones, y f(x)

def graphicPlot(D, A):

    #Funcion utilizada para graficar
    plt.plot(np.array(D), np.array(A))
    plt.title("Gráfico")
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.legend(["Error"])
    plt.show() 

def bolzano(x0,x1):

    #Verificacion del teorema de bolzano
    if(x0*x1 < 0):
        return True
    else:
        return False
