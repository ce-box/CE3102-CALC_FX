from tkinter import * 

def main():
    raiz = Tk() 
    raiz.title("Calculadora") #Cambiar el nombre de la ventana 
    raiz.geometry("520x480") #Configurar tamaño 
    raiz.iconbitmap("images/calc.ico") #Cambiar el icono 
    raiz.config(bg="gray") #Cambiar color de fondo
    raiz.resizable(0,0)
    raiz.mainloop()

main()
