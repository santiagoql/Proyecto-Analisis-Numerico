import streamlit as st
import iterative_methods
import interpolacion_methods
import matplotlib.pyplot as plt

# Personalización de la apariencia general
st.set_page_config(
    page_title="Calculadora de Métodos Numéricos",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título principal
st.markdown(
    """
    <div style="text-align: center; padding: 20px; background-color: #4A90E2; color: white; border-radius: 10px;">
        <h1>Métodos Numéricos Interactivos</h1>
        <p>Resuelve ecuaciones e interpola datos con precisión</p>
    </div>
    """, unsafe_allow_html=True
)

# Barra lateral: Configuración
st.sidebar.title("Configuración")
st.sidebar.markdown("### Ajusta los parámetros para comenzar:")

# Tipo de error
error = st.sidebar.radio(
    "Tipo de Error:",
    ["Decimales Correctos", "Cifras Significativas"],
    index=0,
    help="Selecciona si deseas trabajar con Decimales Correctos o Cifras Significativas."
)

# Número de decimales o cifras significativas
decimals = st.sidebar.slider(
    f"Número de {error}:",
    min_value=1, max_value=10, value=3,
    help="Controla la precisión del cálculo."
)

# Cálculo de tolerancia
tol = 0.5 * 10 ** (-decimals) if error == "Decimales Correctos" else 5 * 10 ** (-decimals)

# Selección del método
method = st.sidebar.selectbox(
    "Selecciona un Método:",
    [
        "Bisección", "Regla Falsa", "Secante", "Newton", "Punto Fijo",
        "Raíces Múltiples 2", "Jacobi", "Gauss-Seidel", "SOR",
        "Spline Lineal", "Spline Cuadrático", "Spline Cúbico",
        "Lagrange", "Diferencias de Newton"
    ],
    help="Elige el método que deseas utilizar."
)

# Mostrar configuración principal
st.markdown("---")
st.markdown(
    f"""
    <div style="background-color: #2C3E50; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: white;">
        <h3>Configuración Actual</h3>
        <ul>
            <li><strong>Tipo de Error:</strong> {error}</li>
            <li><strong>Número de {error.lower()}:</strong> {decimals}</li>
            <li><strong>Tolerancia Calculada:</strong> {tol:.2e}</li>
            <li><strong>Método Seleccionado:</strong> {method}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# Diccionarios de métodos
interpolation_methods = {
    "Lagrange": interpolacion_methods.lagrange_pagina,
    "Diferencias de Newton": interpolacion_methods.diferencias_newton_pagina,
    "Spline Lineal": interpolacion_methods.spline_lineal_pagina,
    "Spline Cuadrático": interpolacion_methods.spline_cuadratico_pagina,
    "Spline Cúbico": interpolacion_methods.spline_cubico_pagina,
}

iterative_methods_dict = {
    "Bisección": iterative_methods.biseccion_pagina,
    "Regla Falsa": iterative_methods.regla_falsa_pagina,
    "Secante": iterative_methods.secante_pagina,
    "Newton": iterative_methods.newton_pagina,
    "Punto Fijo": iterative_methods.punto_fijo_pagina,
    "Raíces Múltiples 2": iterative_methods.raices_multiples_pagina,
    "Jacobi": iterative_methods.jacobi_pagina,
    "Gauss-Seidel": iterative_methods.gauss_seidel_pagina,
    "SOR": iterative_methods.SOR_pagina,
}

# Configuración de columnas para entradas y resultados
st.markdown("### Calculadora")
calculation_container = st.container()

with calculation_container:
    st.write("Por favor, introduce los valores en las columnas correspondientes:")
    if method in interpolation_methods:
        cols = st.columns(2)  # Interpolación requiere 2 columnas
        interpolation_methods[method](cols, error, tol)
    elif method in iterative_methods_dict:
        cols = st.columns(3)  # Iterativos requieren más espacio para ecuaciones
        iterative_methods_dict[method](cols, error, tol)

# Pie de página
st.markdown("---")
st.markdown(
    """
    <footer style="text-align: center; padding: 10px; background-color: #4A90E2; color: white; border-radius: 10px;">
        <p>Desarrollado por [Santiago Quintero Longas] - Métodos Numéricos con Streamlit</p>
    </footer>
    """, unsafe_allow_html=True
)
