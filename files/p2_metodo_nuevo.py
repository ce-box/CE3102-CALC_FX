from sympy import sympify, Symbol

x = Symbol('x')


def dhm(x_0, f, tol=10e-8, iter_max=2500):

    if tol <= 0:
        raise  ValueError('Tolerancia no debe ser cero.')
    f = sympify(f)
    k = 0
    x_k = x_0
    error = tol+1

    while error > tol and k < iter_max:
        x_k = calc_sgte(x_k, f)
        error = calc_error(x_k, f)
        k+=1

    return [x_k,k+1, error]


def calc_error(x_k, f):
    return abs(f.subs(x, x_k))
    

def calc_z(x_k, f):
    f_k = f.subs(x, x_k)
    den = f.subs(x, x_k + f_k) - f.subs(x, x_k - f_k)
    z = x_k + (2* (f_k**2)/den)
    return z


def calc_sgte(x_k, f):
    f_k = f.subs(x, x_k)
    z = calc_z(x_k, f)
    den = f.subs(x, x_k + f_k) - f.subs(x, x_k - f_k)
    x_sgte = x_k - 2*(f_k)*(f.subs(x,z) - f_k)/den
    return round(x_sgte,6)


if __name__ == '__main__':
    # Test 1. Ejemplo (b)
    result = dhm(1.5, 'x^3+4*x^2-10', iter_max=7)
    print(result)

    # Test 2. Ejemplo (h)
    result = dhm(0.7, 'x^2-exp(x)-3*x+2', iter_max=7)
    print(result)

    # Test 3. Ejemplo (e)
    result = dhm(2, 'x^3-10', iter_max=7)
    print(result)

    # Test 4. Ejemplo (c)
    result = dhm(1, 'cos(x)-x', iter_max=6)
    print(result)
