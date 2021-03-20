import tkinter as tk
from tkinter import * 
from parte2_p2 import *
import parte2_p2 as p2
import ast

root = Tk() 

def window():

    root.title("Calculadora") #Cambiar el nombre de la ventana 
    root.geometry("470x430") #Configurar tamaño 
    root.iconbitmap("images/calc.ico") #Cambiar el icono 
    root.config(bg="gray") #Cambiar color de fondo
    root.resizable(0,0)

    selectLbl = Label(root, text="Seleccione un metodo:")
    selectLbl.config(fg="black", bg="gray", font=("Times New Roman",15)) 
    selectLbl.place(x=10, y=10)

    nRaph = tk.Button(root, text="Biseccion",   command= lambda: params(1))
    nRaph.place(x = 10, y = 50)

    nRaph = tk.Button(root, text="Falsa posicion",  command= lambda: params(2))
    nRaph.place(x = 10, y = 90)

    nRaph = tk.Button(root, text="Newton-Raphson",  command= lambda: params(3))
    nRaph.place(x = 10, y = 130)

    nRaph = tk.Button(root, text="Secante",  command= lambda: params(4))
    nRaph.place(x = 10, y = 170)
    
    root.mainloop()

def params(num):

    selectLbl = Label(root, text="Ingrese parametros:")
    selectLbl.config(fg="black", bg="gray", font=("Times New Roman",15)) 
    selectLbl.place(x=275, y=10)
    
    funcLbl = Label(root, text="Funcion f(x)")
    funcLbl.config(fg="black", bg="gray", font=("Times New Roman",12)) 
    funcLbl.place(x=275, y=50)

    func = tk.Entry(root)
    func.place(x=275, y=70)

    tolLbl = Label(root, text="Tolerancia")
    tolLbl.config(fg="black", bg="gray", font=("Times New Roman",12)) 
    tolLbl.place(x=275, y=100)

    tol = tk.Entry(root)
    tol.place(x=275, y=120)

    iterMLbl = Label(root, text="Iteraciones maximas")
    iterMLbl.config(fg="black", bg="gray", font=("Times New Roman",12)) 
    iterMLbl.place(x=275, y=150)

    iterM = tk.Entry(root)
    iterM.place(x=275, y=170)

    if(num == 1 or num == 2):
        
        rangeLbl = Label(root, text="Intervalo")
        rangeLbl.config(fg="black", bg="gray", font=("Times New Roman",12)) 
        rangeLbl.place(x=275, y=200)

        rangeValue = tk.Entry(root)
        rangeValue.place(x=275, y=220)
        
        if(num == 1):
            nRaph = tk.Button(root, text="Calcular",  command= lambda: result(func.get(), ast.literal_eval(rangeValue.get()), eval(tol.get()), int(iterM.get()), 1))
        else:
            nRaph = tk.Button(root, text="Calcular",  command= lambda: result(func.get(), ast.literal_eval(rangeValue.get()), eval(tol.get()), int(iterM.get()), 2))

    elif(num ==  3):

        valueLbl = Label(root, text="Valor inicial")
        valueLbl.config(fg="black", bg="gray", font=("Times New Roman",12)) 
        valueLbl.place(x=275, y=200)

        value = tk.Entry(root)
        value.place(x=275, y=220)

        nRaph = tk.Button(root, text="Calcular",  command= lambda: result(func.get(), eval(value.get()), eval(tol.get()), int(iterM.get()), 3))

    elif(num == 4):

        valuesLbl = Label(root, text="Valores iniciales")
        valuesLbl.config(fg="black", bg="gray", font=("Times New Roman",12)) 
        valuesLbl.place(x=275, y=200)

        value1 = tk.Entry(root)
        value1.config(width=5)
        value1.place(x=275, y=220)

        value2 = tk.Entry(root)
        value2.config(width=5)
        value2.place(x=330, y=220)

        nRaph = tk.Button(root, text="Calcular",  command= lambda: result(func.get(), [eval(value1.get()), eval(value2.get())], eval(tol.get()), int(iterM.get()), 4))
    
    nRaph.place(x = 310, y = 250)
    
def result(func, rango, tol, iterMax, pos):

    if(pos == 1):
        result = p2.biseccion(func, rango, tol, iterMax)
    elif(pos == 2):
        result = p2.falsa_posicion(func, rango, tol, iterMax)
    elif(pos == 3):
        result = p2.newton_raphson(func, rango, tol, iterMax)
    elif(pos == 4):
        result = p2.secante(func, rango[0], rango[1], tol, iterMax)
    

    apprLbl = Label(root, text="Aproximacion de integral:")
    apprLbl.config(fg="black", bg="gray", font=("Times New Roman",15)) 
    apprLbl.place(x=10, y=350)

    approach = tk.Entry(root)
    approach.place(x=225, y=355)
    approach.config(width=25)
    approach.insert(0, str(result[0]))

    errorLbl = Label(root, text="Cota de error:")
    errorLbl.config(fg="black", bg="gray", font=("Times New Roman",15)) 
    errorLbl.place(x=10, y=390)

    error = tk.Entry(root)
    error.place(x=130, y=395)
    error.config(width=25)
    error.insert(0, str(result[1]))

    p2.graphicPlot(result[3], result[4])

window()
