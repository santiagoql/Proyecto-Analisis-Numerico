import numpy as np
import scipy as sp 
import pandas as pd
import matplotlib.pyplot as plt

def tableMat(x_m_list, errores):
    table = pd.DataFrame(x_m_list[1:], columns=x_m_list[0])
    table["Error"] = errores
    return table

def calculate_error(X, X_L, error_rel):
    error = np.max(np.abs(X - X_L))
    if error_rel == 1:
        error = np.max(np.abs((X - X_L) / X))
    elif error_rel == 2:
        error = np.max(np.abs(X - X_L)) / np.max(np.abs(X))
    return error

def radio_espectral(T):
    eig = np.linalg.eigvals(T)
    return np.max(np.abs(eig))

def Jacobi(A, b, X_i, tol, niter, error_rel=False):
    errores = [100]
    n = len(b.split())
    X_val = [["X_" + str(i + 1) for i in range(n)]]

    Am = np.array([list(map(float, row.split())) for row in A.split(';')])
    bm = np.array(list(map(float, b.split())))
    X = np.array(list(map(float, X_i.split())))

    D = np.diag(np.diagonal(Am))
    L = -np.tril(Am, -1)
    U = -np.triu(Am, 1)

    X_val.append(X)

    T = np.linalg.inv(D) @ (L + U)
    C = np.linalg.inv(D) @ bm

    if np.allclose(Am @ X, bm, atol=tol):
        return tableMat(X_val, errores)

    for _ in range(1, niter):
        X_L = X
        X = T @ X + C
        X_val.append(X)

        error = calculate_error(X, X_L, error_rel)
        errores.append(error)

        if error < tol:
            return X, tableMat(X_val, errores), radio_espectral(T)

def Gauss_Seidel(A, b, X_i, tol, niter, error_rel=False):
    errores = [100]
    n = len(b.split())
    X_val = [["X_" + str(i + 1) for i in range(n)]]

    Am = np.array([list(map(float, row.split())) for row in A.split(';')])
    bm = np.array(list(map(float, b.split())))
    X = np.array(list(map(float, X_i.split())))

    D = np.diag(np.diagonal(Am))
    L = -np.tril(Am, -1)
    U = -np.triu(Am, 1)

    X_val.append(X)

    T = np.linalg.inv(D - L) @ U
    C = np.linalg.inv(D - L) @ bm

    if np.allclose(Am @ X, bm, atol=tol):
        return tableMat(X_val, errores)

    for _ in range(1, niter):
        X_L = X
        X = T @ X + C
        X_val.append(X)

        error = calculate_error(X, X_L, error_rel)
        errores.append(error)

        if error < tol:
            return X, tableMat(X_val, errores), radio_espectral(T)

def SOR(A, b, X_i, tol, niter, w, error_rel=False):
    errores = [100]
    n = len(b.split())
    X_val = [["X_" + str(i + 1) for i in range(n)]]

    Am = np.array([list(map(float, row.split())) for row in A.split(';')])
    bm = np.array(list(map(float, b.split())))
    X = np.array(list(map(float, X_i.split())))

    D = np.diag(np.diagonal(Am))
    L = -np.tril(Am, -1)
    U = -np.triu(Am, 1)

    X_val.append(X)

    T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
    C = w * np.linalg.inv(D - w * L) @ bm

    if np.allclose(Am @ X, bm, atol=tol):
        return tableMat(X_val, errores)

    for _ in range(1, niter):
        X_L = X
        X = T @ X + C
        X_val.append(X)

        error = calculate_error(X, X_L, error_rel)
        errores.append(error)

        if error < tol:
            return X, tableMat(X_val, errores), radio_espectral(T)
