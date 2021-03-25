import tkinter as tk 
from tkinter import *
from parte2_p2 import *
import parte2_p2 as p2
from p2_metodo_nuevo import *
import p2_metodo_nuevo as p1
import ast

root = Tk() #Inicializa ventana
labels = [] #Lista de labels (para borrar)
results = [] #Lista de labels (display de resultados)

#Imagen para display de resultados
dispImage = PhotoImage(file = "images/disp.png")
bg = Label(root, image = dispImage)
bg.place(x = 110, y =  20)

#Canvas para display de resultados
canvas = tk.Canvas(root, bg = "black", width=245.5, height=85.6)
canvas.place(x = 112.3, y = 22.3)

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

    #Boton para seleccionar el metodo de la biseccion
    bisect = tk.Button(root, text="Biseccion", width = 20, command= lambda: params(1, "Biseccion"))
    bisect.place(x = 10, y = 220)

    #Boton para selecionar el metodo de la falsa posicion
    fPos = tk.Button(root, text="Falsa posicion", width = 20, command= lambda: params(2, "Falsa Posicion"))
    fPos.place(x = 10, y = 260)

    #Boton para seleccionar el metodo de Newton-Raphson
    nRaph = tk.Button(root, text="Newton-Raphson", width = 20, command= lambda: params(3, "Newton-Raphson"))
    nRaph.place(x = 10, y = 300)

    #Boton para seleccionar el metodo de la secante
    sec = tk.Button(root, text="Secante", width = 20, command= lambda: params(4, "Secante"))
    sec.place(x = 10, y = 340)

    #Boton para seleccionar el nuevo metodo
    nMeth = tk.Button(root, text="Nuevo Metodo", width = 20, command= lambda: params(5, "Nuevo Metodo"))
    nMeth.place(x = 10, y = 380)

    #Boton para mostrar el manual de usuario de la calculadora
    manual = tk.Button(root, text="Ayuda", command = manualGuide)
    manual.place(x = 40, y = 20)

    #Inicializacion de la ventana
    root.mainloop()


def manualGuide():

    #Muestra el manual de usuario
    tk.messagebox.showinfo(message=
                           ("Manual de Usuario \n"
                           + "1. Seleccione el método a utilizar (columna derecha) \n"
                           + "2. Una vez seleccionado el método, ingrese los parámetros de forma correcta \n"
                           + "3. De no haber ingresado los parámetros de forma correcta, se mostrará un mensaje de error \n"
                           + "4. Habiendo digitado los parámetros correctamente, presione el botón “calcular” \n"
                           + "5. Se le mostrará en el display los resultados: Aproximación al cero, error absoluto, iteraciones \n"
                           + "6. Seguidamente puede visualizar la gráfica presionando sobre el botón de “gráfica” \n"
                           + "7. Puede seguir utilizando los métodos disponibles siguiendo los nuevamente los pasos del 2 al 7")
                           , title="Guia")


def params(num, mType):

    global labels
    global results

    #Elimina todos los labels para crear nuevos (en caso de posible superposicion)
    if(len(labels) > 0):
        for label in labels:
            label.destroy()

    #Elimina los labels de resultados para limpiar resultados (en caso de posible superposicion)
    for result in results:
        result.destroy()

    #Label del metodo seleccionado
    methType = Label(root, text=mType)
    methType.config(fg="deep sky blue", bg="black", font=("Times New Roman",10)) 
    methType.place(x=205, y=30)
    labels.append(methType)

    #Label para el resultado de la aproximacion
    methAprox = Label(root, text="Aprox:")
    methAprox.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methAprox.place(x=120, y=55)
    results.append(methAprox)

    #Label para el resultado de error
    methError = Label(root, text="Error:")
    methError.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methError.place(x=120, y=80)
    results.append(methError)

    #Label para el registro de iteraciones
    methIter = Label(root, text="Iter:")
    methIter.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methIter.place(x=300, y=80)
    results.append(methIter)

    #Label de instruccion
    selectLbl = Label(root, text="Ingrese parametros:")
    selectLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",15)) 
    selectLbl.place(x=275, y=180)
    labels.append(selectLbl)

    #Label y text-box para ingresar funcion
    funcLbl = Label(root, text="Funcion f(x)")
    funcLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
    funcLbl.place(x=275, y=220)
    labels.append(funcLbl)

    func = tk.Entry(root)
    func.place(x=275, y=240)
    labels.append(func)

    #Label y text-box para ingresar funcion
    tolLbl = Label(root, text="Tolerancia")
    tolLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
    tolLbl.place(x=275, y=270)
    labels.append(tolLbl)

    tol = tk.Entry(root)
    tol.place(x=275, y=290)
    labels.append(tol)

    #Label y text-box para ingresar funcion
    iterMLbl = Label(root, text="Iteraciones maximas")
    iterMLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
    iterMLbl.place(x=275, y=320)
    labels.append(iterMLbl)

    iterM = tk.Entry(root)
    iterM.place(x=275, y=340)
    labels.append(iterM)

    #En caso de haber seleccionado Biseccion o Falsa posicion
    if(num == 1 or num == 2):

        #Label y text-box para ingresar el rango
        rangeLbl = Label(root, text="Intervalo")
        rangeLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
        rangeLbl.place(x=275, y=370)
        labels.append(rangeLbl)

        rangeValue = tk.Entry(root)
        rangeValue.place(x=275, y=390)
        labels.append(rangeValue)

        #Verifica los datos ingresados dependiendo del metodo seleccionado (Biseccion o Falsa posicion)
        if(num == 1):
            calc = tk.Button(root, text="Calcular",  command= lambda: check(func.get(), rangeValue.get(), tol.get(), iterM.get(), 1))
        else:
            calc = tk.Button(root, text="Calcular",  command= lambda: check(func.get(), rangeValue.get(), tol.get(), iterM.get(), 2))

    #En caso de haber seleccionado Biseccion o falsa posicion
    elif(num ==  3 or num == 5):

        #Label y text-box para ingresar el valor inicial
        valueLbl = Label(root, text="Valor inicial")
        valueLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
        valueLbl.place(x=275, y=370)
        labels.append(valueLbl)

        value = tk.Entry(root)
        value.place(x=275, y=390)
        labels.append(value)

        #Verifica los datos ingresados dependiendo del metodo seleccionado (Newton-Raphson o Nuevo Metodo)
        if(3):
            calc = tk.Button(root, text="Calcular",  command= lambda: check(func.get(),value.get(), tol.get(), iterM.get(), 3))
        else:
            calc = tk.Button(root, text="Calcular",  command= lambda: check(func.get(),value.get(), tol.get(), iterM.get(), 5))

    elif(num == 4):

        #Label y text-box para ingresar los valores iniciales
        valuesLbl = Label(root, text="Valores iniciales")
        valuesLbl.config(fg="black", bg="deep sky blue", font=("Times New Roman",12)) 
        valuesLbl.place(x=275, y=370)
        labels.append(valuesLbl)

        #Primer valor
        value1 = tk.Entry(root)
        value1.config(width=5)
        value1.place(x=275, y=390)
        labels.append(value1)
        
        #Segundo valor
        value2 = tk.Entry(root)
        value2.config(width=5)
        value2.place(x=330, y=390)
        labels.append(value2)

        #Verifica los datos ingresados para el metodo de la secante
        calc = tk.Button(root, text="Calcular",  command= lambda: check(func.get(), [value1.get(), value2.get()], tol.get(), iterM.get(), 4))

    calc.place(x = 390, y = 20)

def check(func, rango, tol, iterM, num):

    #Verifica la validez de todos los datos ingresados
    try:
        
        if(num == 1 or  num == 2):

            #Verifica rango (Biseccion - Falsa Posicion)
            rango = ast.literal_eval(rango)
            
        elif(num == 3 or num == 5):

            #Verifica valor inicial (Newton-Raphson)
            rango = eval(rango)
            
        elif(num == 4):

            #Verifica valores iniciales (Secante)
            rango = [eval(rango[0]), eval(rango[1])]
            
        #Verifica tolerancia
        tol = eval(tol)

        #Verifica iteraciones maximas
        iterM = int(iterM)

        #Llama a la funcion de resultado con los parametros ingresados
        result(func, rango, tol, iterM, num)
        
    except:

        #Mensaje de error en caso de encontrar alguno
        tk.messagebox.showinfo(message="Error al digitar la funcion", title="ERROR")
    
  
def result(func, rango, tol, iterMax, pos):

    global results

    #Limpia los labels de resultados (Para ingresar los mismos con la adicion de los resultados)
    for result in results:
        result.destroy()

    #Llama al metodo seleccionado
    if(pos == 1):

        #Biseccion
        result = p2.biseccion(func, rango, tol, iterMax)
        
    elif(pos == 2):

        #Falsa Posicion
        result = p2.falsa_posicion(func, rango, tol, iterMax)
        
    elif(pos == 3):

        #Newton-Raphson
        result = p2.newton_raphson(func, rango, tol, iterMax)
        
    elif(pos == 4):

        #Secante
        result = p2.secante(func, rango[0], rango[1], tol, iterMax)

    elif(pos == 5):

        #Metodo Nuevo
        result = p1.metodo_nuevo(func, rango, tol, iterMax)
    
    #Crea el label de la aproximacion con su resultado
    methAprox = Label(root, text=("Aprox: " + str(result[0])))
    methAprox.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methAprox.place(x=120, y=55)
    results.append(methAprox)

    #Crea el label del error con su resultado
    methError = Label(root, text="Error: " + str(result[1]))
    methError.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methError.place(x=120, y=80)
    results.append(methError)

    #Crea el label de las iteraciones con su resultado
    methIter = Label(root, text="Iter:" + str(result[2]))
    methIter.config(fg="white", bg="black", font=("Times New Roman",8)) 
    methIter.place(x=300, y=80)
    results.append(methIter)

    #Boton para graficar    
    gPlot = tk.Button(root, text="Graficar",  command= lambda: graphic(result[3], result[4]))
    gPlot.place(x = 390, y = 50)

def graphic(A,D):

    #Llama al metodo para graficar, con las iteraciones y los errores
    p2.graphicPlot(A, D)


params(1, "Biseccion") #Llama a params con el metodo biseccion (como predeterminado)
window() #Llama a la ventana principal
