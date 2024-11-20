import numpy as np
import sympy
from utils import parse_pol

def lagrange(x, y):
    n = len(x)
    tabla = np.zeros((n, n))
    for i in range(n):
        Li = 1
        den = 1
        for j in range(n):
            if j != i:
                paux = [1, -x[j]]
                Li = np.convolve(Li, paux)
                den *= x[i] - x[j]

        tabla[i, :] = y[i] * Li / den

    pols = [sum(tabla).tolist()]
    polinomio = parse_pol(pols)
    return polinomio, pols


def diferencias_newton(x, y):
    n = len(x)
    tabla = np.zeros((n, n + 1))
    tabla[:, 0] = x
    tabla[:, 1] = y
    for j in range(2, n + 1):
        for i in range(j - 1, n):
            denominador = tabla[i, 0] - tabla[i - j + 1, 0]
            tabla[i, j] = (tabla[i, j - 1] - tabla[i - 1, j - 1]) / denominador

    pol = 0
    coef = np.diag(tabla[:, 1:])
    x_symbol = sympy.Symbol("x")
    for i in range(len(coef)):
        const = coef[i]
        for j in range(i):
            const *= x_symbol - x[j]
        pol += const

    return [str(sympy.simplify(pol))], tabla.tolist()


def spline_lineal(x, y):
    n = len(x)
    d = 1
    m = (d + 1) * (n - 1)

    A = np.zeros((m, m))
    b = np.zeros((m, 1))

    # Condiciones del spline
    for i in range(n - 1):
        A[i, i * 2] = x[i]
        A[i, i * 2 + 1] = 1
        b[i] = y[i]

        A[i + n - 1, i * 2] = x[i + 1]
        A[i + n - 1, i * 2 + 1] = 1
        b[i + n - 1] = y[i + 1]

    coef = np.linalg.solve(A, b).flatten()
    pols = coef.reshape(n - 1, d + 1)
    polinomios = parse_pol(pols)
    return polinomios, pols.tolist()


def spline_cuadratico(x, y):
    n = len(x)
    d = 2
    m = (d + 1) * (n - 1)

    A = np.zeros((m, m))
    b = np.zeros((m, 1))

    for i in range(n - 1):
        A[i, i * 3:(i + 1) * 3] = [x[i]**2, x[i], 1]
        b[i] = y[i]

        A[i + n - 1, i * 3:(i + 1) * 3] = [x[i + 1]**2, x[i + 1], 1]
        b[i + n - 1] = y[i + 1]

    for i in range(1, n - 1):
        A[2 * n - 3 + i, (i - 1) * 3:(i + 1) * 3] = [2 * x[i], 1, 0, -2 * x[i], -1, 0]

    A[-1, 0] = 2

    coef = np.linalg.solve(A, b).flatten()
    pols = coef.reshape(n - 1, d + 1)
    polinomios = parse_pol(pols)
    return polinomios, pols.tolist()


def spline_cubico(x, y):
    n = len(x)
    d = 3
    m = (d + 1) * (n - 1)

    A = np.zeros((m, m))
    b = np.zeros((m, 1))

    for i in range(n - 1):
        A[i, i * 4:(i + 1) * 4] = [x[i]**3, x[i]**2, x[i], 1]
        b[i] = y[i]

        A[i + n - 1, i * 4:(i + 1) * 4] = [x[i + 1]**3, x[i + 1]**2, x[i + 1], 1]
        b[i + n - 1] = y[i + 1]

    for i in range(1, n - 1):
        A[2 * n - 2 + (i - 1), (i - 1) * 4:(i + 1) * 4] = [
            3 * x[i]**2, 2 * x[i], 1, 0, -3 * x[i]**2, -2 * x[i], -1, 0]

        A[3 * n - 4 + (i - 1), (i - 1) * 4:(i + 1) * 4] = [
            6 * x[i], 2, 0, 0, -6 * x[i], -2, 0, 0]

    A[-2, 0:2] = [6 * x[0], 2]
    A[-1, -4:-2] = [6 * x[-1], 2]

    coef = np.linalg.solve(A, b).flatten()
    pols = coef.reshape(n - 1, d + 1)
    polinomios = parse_pol(pols)
    return polinomios, pols.tolist()
