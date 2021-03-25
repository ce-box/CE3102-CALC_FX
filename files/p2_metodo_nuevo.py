from sympy import sympify, Symbol

x = Symbol('x') #Se comvierte la variable a simbolico

#Funcion principal del metodo
def metodo_nuevo(x_0, f, tol=10e-8, iter_max=2500):

    if tol <= 0:
        raise  ValueError('Tolerancia no debe ser cero.') #Error al ingresar una tolerancia con las condiones no aptas
    f = sympify(f)
    k = 0
    x_k = x_0
    error = tol+1

    # Cliclo de iteraciones segun tolerancia o maximo de iteraciones
    while error > tol and k < iter_max:
        x_k = calc_sgte(x_k, f)
        error = calc_error(x_k, f)
        k+=1

    return [x_k,k+1, error]

#Calcula el error 
def calc_error(x_k, f):
    return abs(f.subs(x, x_k))
    
#Calcula la variable Z al ser una expresion tan grande
def calc_z(x_k, f):
    f_k = f.subs(x, x_k)
    den = f.subs(x, x_k + f_k) - f.subs(x, x_k - f_k)
    z = x_k + (2* (f_k**2)/den)
    return z

#Realiza el calculo de Xk+1 
def calc_sgte(x_k, f):
    f_k = f.subs(x, x_k)
    z = calc_z(x_k, f)#Invoca la funcion para calcular el valor de Z
    den = f.subs(x, x_k + f_k) - f.subs(x, x_k - f_k)
    x_sgte = x_k - 2*(f_k)*(f.subs(x,z) - f_k)/den
    return round(x_sgte,6) #Restinge la cantidad de decimales a 5


if __name__ == '__main__':
    # Cada caso de prueba recibe: valor de X0, Ecuacion y numero de iteraciones maximas
    # Test 1. Ejemplo (b)
    result = metodo_nuevo(1.5, 'x^3+4*x^2-10', iter_max=7)
    print(result)

    # Test 2. Ejemplo (h)
    result = metodo_nuevo(0.7, 'x^2-exp(x)-3*x+2', iter_max=7)
    print(result)

    # Test 3. Ejemplo (e)
    result = metodo_nuevo(2, 'x^3-10', iter_max=7)
    print(result)

    # Test 4. Ejemplo (c)
    result = metodo_nuevo(1, 'cos(x)-x', iter_max=6)
    print(result)
