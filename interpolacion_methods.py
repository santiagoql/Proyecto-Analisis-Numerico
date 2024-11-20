import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from interpolacion import (
    lagrange,
    diferencias_newton,
    spline_lineal,
    spline_cuadratico,
    spline_cubico
)
from utils import parse_pol

def mostrar_ayuda_interpolacion():
    st.sidebar.markdown("## Ayuda de Interpolación")
    with st.sidebar.expander("Formato de entrada para puntos"):
        st.write("""
        - Ingrese los puntos en el formato x1,y1; x2,y2; ...
        - Asegúrese de que los puntos estén separados por comas y cada par de puntos esté separado por un punto y coma.
        - Ejemplo: 0,0; 1,2; 2,0
        """)
    with st.sidebar.expander("Errores comunes"):
        st.write("""
        - Formato incorrecto: Verifique que los puntos estén en el formato correcto.
        - Puntos duplicados: Asegúrese de que no haya puntos duplicados.
        """)

def lagrange_pagina(cols, error, tol):
    if len(cols) != 2:
        st.error("Se necesitan exactamente dos columnas")
        return
    col1, col2 = cols
    with col1:
        puntos = st.text_input('Ingrese los puntos (formato x1,y1; x2,y2; ...)', value="8,17; 15,29; 23,148; 36,34; 40,10")

    try:
        puntos_list = [tuple(map(float, punto.split(','))) for punto in puntos.split(';')]
        x, y = zip(*puntos_list)
    except ValueError:
        st.error("Error: Asegúrate de ingresar los puntos en el formato correcto y sin caracteres inválidos.")
        return

    try:
        polinomio, pols = lagrange(list(x), list(y))
        st.write("Polinomio de Lagrange:")
        st.write(polinomio)
        st.write("Coeficientes de Lagrange:")
        st.write(pols)
    except ValueError as e:
        st.error(f"Error al calcular el polinomio de Lagrange: {e}")

def diferencias_newton_pagina(cols, error, tol):
    if len(cols) != 2:
        st.error("Se necesitan exactamente dos columnas")
        return
    col1, col2 = cols
    with col1:
        puntos = st.text_input('Ingrese los puntos (formato x1,y1; x2,y2; ...)', value="8,17; 15,29; 23,148; 36,34; 40,10")

    try:
        puntos_list = [tuple(map(float, punto.split(','))) for punto in puntos.split(';')]
        x, y = zip(*puntos_list)
    except ValueError:
        st.error("Error: Asegúrate de ingresar los puntos en el formato correcto y sin caracteres inválidos.")
        return

    try:
        polinomio, tabla = diferencias_newton(list(x), list(y))
        st.write("Polinomio de Diferencias de Newton:")
        st.write(polinomio)
        st.write("Tabla de Diferencias:")
        st.write(tabla)
    except ValueError as e:
        st.error(f"Error al calcular el polinomio de diferencias de Newton: {e}")

def spline_lineal_pagina(cols, error, tol):
    if len(cols) != 2:
        st.error("Se necesitan exactamente dos columnas")
        return
    col1, col2 = cols
    with col1:
        puntos = st.text_input('Ingrese los puntos (formato x1,y1; x2,y2; ...)', value="8,17; 15,29; 23,148; 36,34; 40,10")

    try:
        puntos_list = [tuple(map(float, punto.split(','))) for punto in puntos.split(';')]
        x, y = zip(*puntos_list)
    except ValueError:
        st.error("Error: Asegúrate de ingresar los puntos en el formato correcto y sin caracteres inválidos.")
        return

    try:
        polinomios, pols = spline_lineal(list(x), list(y))
        st.write("Polinomios Lineales del Spline:")
        st.write(polinomios)
        st.write("Coeficientes de los Polinomios:")
        st.write(pols)
    except ValueError as e:
        st.error(f"Error al calcular el spline lineal: {e}")

def spline_cuadratico_pagina(cols, error, tol):
    if len(cols) != 2:
        st.error("Se necesitan exactamente dos columnas")
        return
    col1, col2 = cols
    with col1:
        puntos = st.text_input('Ingrese los puntos (formato x1,y1; x2,y2; ...)', value="8,17; 15,29; 23,148; 36,34; 40,10")

    try:
        puntos_list = [tuple(map(float, punto.split(','))) for punto in puntos.split(';')]
        x, y = zip(*puntos_list)
    except ValueError:
        st.error("Error: Asegúrate de ingresar los puntos en el formato correcto y sin caracteres inválidos.")
        return

    try:
        polinomios, pols = spline_cuadratico(list(x), list(y))
        st.write("Polinomios Cuadráticos del Spline:")
        st.write(polinomios)
        st.write("Coeficientes de los Polinomios:")
        st.write(pols)
    except ValueError as e:
        st.error(f"Error al calcular el spline cuadrático: {e}")

def spline_cubico_pagina(cols, error, tol):
    if len(cols) != 2:
        st.error("Se necesitan exactamente dos columnas")
        return
    col1, col2 = cols
    with col1:
        puntos = st.text_input('Ingrese los puntos (formato x1,y1; x2,y2; ...)', value="8,17; 15,29; 23,148; 36,34; 40,10")

    try:
        puntos_list = [tuple(map(float, punto.split(','))) for punto in puntos.split(';')]
        x, y = zip(*puntos_list)
    except ValueError:
        st.error("Error: Asegúrate de ingresar los puntos en el formato correcto y sin caracteres inválidos.")
        return

    try:
        polinomios, pols = spline_cubico(list(x), list(y))
        st.write("Polinomios Cúbicos del Spline:")
        st.write(polinomios)
        st.write("Coeficientes de los Polinomios:")
        st.write(pols)
    except ValueError as e:
        st.error(f"Error al calcular el spline cúbico: {e}")
