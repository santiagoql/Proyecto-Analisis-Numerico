import streamlit as st
import pandas as pd
import numpy as np
import iterative_methods
import math

st.title('Metodos Numericos')

col1, col2= st.columns([1,1])

with col1:
    error = st.selectbox(
    "Quieres utilizar Cifras Significativas o Decimales Correctos?",
    ("Decimales Correctos", "Cifras Significatias"),
)

with col2:
    decimals = st.number_input(f'Ingrese el número de {error}', min_value=1, max_value=10, value=3)

if error == "Decimales Correctos":
    tol = 0.5 * 10 ** (-decimals)
else:
    tol = 5 * 10 ** (-decimals)

method = st.selectbox(
"Que metodo quieres utilizar?",
("Biseccion", "Regla Falsa", "Secante", "Newton", "Punto Fijo", "Raices Multiples 2", "Jacobi", "Gauss_Seidel", "SOR"),)

methods = {
    "Biseccion": iterative_methods.biseccion_pagina,
    "Regla Falsa": iterative_methods.regla_falsa_pagina,
    "Secante": iterative_methods.secante_pagina,
    "Newton": iterative_methods.newton_pagina,
    "Punto Fijo": iterative_methods.punto_fijo_pagina,
    "Raices Multiples 2":iterative_methods.raices_multiples2_pagina,
    "Jacobi":iterative_methods.jacobi_pagina,
    "Gauss_Seidel":iterative_methods.gauss_seidel_pagina,
    "SOR":iterative_methods.SOR_pagina
}
if method in ["Biseccion", "Regla Falsa", "Secante", "Punto Fijo"]:
    cols = st.columns([1,1,1])
if method in ["Newton",  "Raices Multiples 2"]:
    cols = st.columns([1,1])
if method in ["Jacobi", "Gauss_Seidel", "SOR"]:
    cols = st.columns([1,1])

methods[method](cols, error,tol)
