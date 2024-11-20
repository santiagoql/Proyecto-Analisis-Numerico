import numpy as np
import pandas as pd
from scipy.misc import derivative
import matplotlib.pyplot as plt

def biseccion(function, a, b, tol, n, use_sig_digits=False):
    # Verificar que la función es continua en [a, b]
    if function(a) * function(b) >= 0:
        print(f"El intervalo [{a},{b}] es inadecuado.")
        return None, None

    errors = [100]
    x_m_list = []
    f_list = []

    for i in range(n):
        x_m = (a + b) / 2
        x_m_list.append(x_m)
        f_x_m = function(x_m)
        f_list.append(f_x_m)

        if f_x_m == 0:
            return x_m, table(x_m_list, f_list, errors)

        if function(a) * f_x_m < 0:
            b = x_m
        else:
            a = x_m

        if i > 0:
            error = calculate_error(use_sig_digits, x_m, x_m_list, i)
            errors.append(error)
            if error < tol:
                plot_results(function, x_m_list)
                return x_m, table(x_m_list, f_list, errors)

    plot_results(function, x_m_list)
    return None, table(x_m_list, f_list, errors)

def regla_falsa(function, a, b, tol, n, use_sig_digits=False):
    if function(a) * function(b) >= 0:
        print(f"El intervalo [{a},{b}] es inadecuado.")
        return None, None

    errors = [100]
    x_m_list = []
    f_list = []

    for i in range(n):
        x_m = b - function(b) * ((b - a) / (function(b) - function(a)))
        x_m_list.append(x_m)
        f_x_m = function(x_m)
        f_list.append(f_x_m)

        if f_x_m == 0:
            return x_m, table(x_m_list, f_list, errors)

        if function(a) * f_x_m < 0:
            b = x_m
        else:
            a = x_m

        if i > 0:
            error = calculate_error(use_sig_digits, x_m, x_m_list, i)
            errors.append(error)
            if error < tol:
                plot_results(function, x_m_list)
                return x_m, table(x_m_list, f_list, errors)

    plot_results(function, x_m_list)
    return None, table(x_m_list, f_list, errors)

def secante(function, x0, x1, tol, n, use_sig_digits=False):
    errors = [100]
    x_m_list = []
    f_list = []

    for i in range(n):
        x_m_new = x1 - (function(x1) * (x1 - x0)) / (function(x1) - function(x0))
        x0, x1 = x1, x_m_new
        x_m_list.append(x1)
        f_x_m = function(x1)
        f_list.append(f_x_m)

        if f_x_m == 0:
            return x1, table(x_m_list, f_list, errors)

        if i > 0:
            error = calculate_error(use_sig_digits, x1, x_m_list, i)
            errors.append(error)
            if error < tol:
                plot_results(function, x_m_list)
                return x1, table(x_m_list, f_list, errors)

    plot_results(function, x_m_list)
    return None, table(x_m_list, f_list, errors)

def newton(function, x0, tol, n, use_sig_digits=False):
    errors = [100]
    x_m_list = []
    f_list = []
    
    for i in range(n):
        df = derivative(function, x0, dx=1e-6)
        if df == 0:
            print("La derivada es cero, el método no puede continuar.")
            break
        x0 = x0 - function(x0) / df
        x_m_list.append(x0)
        f_x_m = function(x0)
        f_list.append(f_x_m)

        if f_x_m == 0:
            return x0, table(x_m_list, f_list, errors)

        if i > 0:
            error = calculate_error(use_sig_digits, x0, x_m_list, i)
            errors.append(error)
            if error < tol:
                plot_results(function, x_m_list)
                return x0, table(x_m_list, f_list, errors)

    plot_results(function, x_m_list)
    return None, table(x_m_list, f_list, errors)

def punto_fijo(function, g, x0, tol, n, use_sig_digits=False):
    errors = [100]
    x_m_list = []
    f_list = []

    for i in range(n):
        x0 = g(x0)
        x_m_list.append(x0)
        f_x_m = function(x0)
        f_list.append(f_x_m)

        if f_x_m == 0:
            return x0, table(x_m_list, f_list, errors)

        if i > 0:
            error = calculate_error(use_sig_digits, x0, x_m_list, i)
            errors.append(error)
            if error < tol:
                plot_results(function, x_m_list)
                return x0, table(x_m_list, f_list, errors)

    plot_results(function, x_m_list)
    return None, table(x_m_list, f_list, errors)

def raices_multiples(function, x0, tol, n, use_sig_digits=False):
    errors = [100]
    x_m_list = []
    f_list = []

    for i in range(n):
        df = derivative(function, x0, dx=1e-6)
        d2f = derivative(lambda x: derivative(function, x, dx=1e-6), x0, dx=1e-6)
        denom = (df**2 - function(x0) * d2f)
        if denom == 0:
            print("El denominador es cero, el método no puede continuar.")
            break

        x0 = x0 - (function(x0) * df) / denom
        x_m_list.append(x0)
        f_x_m = function(x0)
        f_list.append(f_x_m)

        if f_x_m == 0:
            return x0, table(x_m_list, f_list, errors)

        if i > 0:
            error = calculate_error(use_sig_digits, x0, x_m_list, i)
            errors.append(error)
            if error < tol:
                plot_results(function, x_m_list)
                return x0, table(x_m_list, f_list, errors)

    plot_results(function, x_m_list)
    return None, table(x_m_list, f_list, errors)

def calculate_error(use_sig_digits, x_m, x_list, index):
    if use_sig_digits:
        error = abs((x_m - x_list[index - 1]) / x_m) * 100
    else:
        error = abs(x_m - x_list[index - 1])
    return error

def table(x_m_list, f_list, errors):
    return pd.DataFrame({
        'X_m': x_m_list,
        'f(X_m)': f_list,
        'Error': errors
    })

def plot_results(function, x_m_list):
    x_vals = np.linspace(min(x_m_list) - 1, max(x_m_list) + 1, 500)
    y_vals = function(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue")
    plt.scatter(x_m_list, [function(x) for x in x_m_list], color="red", label="Iteraciones")
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.title("Gráfico de la función y puntos iterados")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()
