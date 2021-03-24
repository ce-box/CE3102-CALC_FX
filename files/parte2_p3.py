import tkinter as tk
from tkinter import *
from parte2_p2 import *
import parte2_p2 as p2
import ast


root = Tk() #Inicializa ventana
labels = [] #Lista de labels (para borrar)
results = []

dispImage = PhotoImage(file = "images/disp.png")
bg = Label(root, image = dispImage)
bg.place(x = 110, y =  20)

canvas = tk.Canvas(root, bg = "black", width=245.5, height=85.6)
canvas.place(x = 112.3, y = 22.3)

methType = Label(root, text="Biseccion")
methType.config(fg="white", bg="black", font=("Times New Roman",8)) 
methType.place(x=120, y=30)
labels.append(methType)

methAprox = Label(root, text="Aprox:")
methAprox.config(fg="white", bg="black", font=("Times New Roman",8)) 
methAprox.place(x=120, y=55)
results.append(methAprox)

methError = Label(root, text="Error:")
methError.config(fg="white", bg="black", font=("Times New Roman",8)) 
methError.place(x=120, y=80)
results.append(methError)

def window():

    #Especificaciones de ventana
    root.title("Calculadora")  
    root.geometry("470x430") 
    root.iconbitmap("images/calc.ico") 
    root.config(bg="deep sky blue") 
    root.resizable(0,0)

    #Label de seleccion
    selectLbl = Label(root, text="Seleccione un metodo:")
    selectLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",15)) 
    selectLbl.place(x=10, y=180)

    #Boton para seleccionar Newton-Raphson
    bisect = tk.Button(root, text="Biseccion", width = 20, command= lambda: params(1, "Biseccion"))
    bisect.place(x = 10, y = 220)

    fPos = tk.Button(root, text="Falsa posicion", width = 20, command= lambda: params(2, "Falsa Posicion"))
    fPos.place(x = 10, y = 260)

    nRaph = tk.Button(root, text="Newton-Raphson", width = 20, command= lambda: params(3, "Newton-Raphson"))
    nRaph.place(x = 10, y = 300)

    sec = tk.Button(root, text="Secante", width = 20, command= lambda: params(4, "Secante"))
    sec.place(x = 10, y = 340)

    manual = tk.Button(root, text="Ayuda", command = manualFile)
    manual.place(x = 40, y = 20)
    
    root.mainloop()


def manualFile():
    global path
    wb.open_new(r'C:\Users\Admin\Desktop\Semestre 1 2021\ANPI\Tarea 1\Calc-repo\CE3102-CALC_FX\files\docs.pdf')

def params(num, mType):

    global labels
    global results

    if(len(labels) > 0):
        for label in labels:
            label.destroy()

    for result in results:
        result.destroy()

    methAprox = Label(root, text=("Aprox: "))
    methAprox.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methAprox.place(x=120, y=55)
    results.append(methAprox)

    methError = Label(root, text="Error: ")
    methError.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methError.place(x=120, y=80)
    results.append(methError)

    methType = Label(root, text=mType)
    methType.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methType.place(x=120, y=30)
    labels.append(methType)

    selectLbl = Label(root, text="Ingrese parametros:")
    selectLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",15)) 
    selectLbl.place(x=275, y=180)
    labels.append(selectLbl)
    
    funcLbl = Label(root, text="Funcion f(x)")
    funcLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
    funcLbl.place(x=275, y=220)
    labels.append(funcLbl)

    func = tk.Entry(root)
    func.place(x=275, y=240)
    labels.append(func)

    tolLbl = Label(root, text="Tolerancia")
    tolLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
    tolLbl.place(x=275, y=270)
    labels.append(tolLbl)

    tol = tk.Entry(root)
    tol.place(x=275, y=290)
    labels.append(tol)

    iterMLbl = Label(root, text="Iteraciones maximas")
    iterMLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
    iterMLbl.place(x=275, y=320)
    labels.append(iterMLbl)

    iterM = tk.Entry(root)
    iterM.place(x=275, y=340)
    labels.append(iterM)

    if(num == 1 or num == 2):
        
        rangeLbl = Label(root, text="Intervalo")
        rangeLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
        rangeLbl.place(x=275, y=370)
        labels.append(rangeLbl)

        rangeValue = tk.Entry(root)
        rangeValue.place(x=275, y=390)
        labels.append(rangeValue)
        
        if(num == 1):
            nRaph = tk.Button(root, text="Calcular",  command= lambda: check(func.get(), rangeValue.get(), tol.get(), iterM.get(), 1))
        else:
            nRaph = tk.Button(root, text="Calcular",  command= lambda: check(func.get(), rangeValue.get(), tol.get(), iterM.get(), 2))

    elif(num ==  3):

        valueLbl = Label(root, text="Valor inicial")
        valueLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
        valueLbl.place(x=275, y=370)
        labels.append(valueLbl)

        value = tk.Entry(root)
        value.place(x=275, y=390)
        labels.append(value)

        nRaph = tk.Button(root, text="Calcular",  command= lambda: check(func.get(),value.get(), tol.get(), iterM.get(), 3))

    elif(num == 4):

        valuesLbl = Label(root, text="Valores iniciales")
        valuesLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
        valuesLbl.place(x=275, y=370)
        labels.append(valuesLbl)

        value1 = tk.Entry(root)
        value1.config(width=5)
        value1.place(x=275, y=390)
        labels.append(value1)

        value2 = tk.Entry(root)
        value2.config(width=5)
        value2.place(x=330, y=390)
        labels.append(value2)

        nRaph = tk.Button(root, text="Calcular",  command= lambda: check(func.get(), [value1.get(), value2.get()], tol.get(), iterM.get(), 4))
    
    nRaph.place(x = 390, y = 20)

def check(func, rango, tol, iterM, num):

    try:
        
        if(num == 1 or  num == 2):
            rango = ast.literal_eval(rango)
        elif(num == 3):
            rango = eval(rango)
        elif(num == 4):
            rango = [eval(rango[0]), eval(rango[1])]

        tol = eval(tol)

        iterM = int(iterM)

        result(func, rango, tol, iterM, num)
        
    except:

        tk.messagebox.showinfo(message="Error al digitar la funcion", title="ERROR")
    
  
def result(func, rango, tol, iterMax, pos):

    global results

    for result in results:
        result.destroy()
    
    if(pos == 1):
        result = p2.biseccion(func, rango, tol, iterMax)
    elif(pos == 2):
        result = p2.falsa_posicion(func, rango, tol, iterMax)
    elif(pos == 3):
        result = p2.newton_raphson(func, rango, tol, iterMax)
    elif(pos == 4):
        result = p2.secante(func, rango[0], rango[1], tol, iterMax)
    

    methAprox = Label(root, text=("Aprox: " + str(result[0])))
    methAprox.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methAprox.place(x=120, y=55)
    results.append(methAprox)

    methError = Label(root, text="Error: " + str(result[1]))
    methError.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methError.place(x=120, y=80)
    results.append(methError)

    gPlot = tk.Button(root, text="Graficar",  command= lambda: graphic(result[3], result[4]))
    gPlot.place(x = 390, y = 50)

def graphic(A,D):

    p2.graphicPlot(A, D)

params(1, "Biseccion")
window()
