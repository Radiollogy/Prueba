import streamlit as st
import random

# Función para generar una ecuación aleatoria de primer grado
def generar_ecuacion():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    x = random.randint(-10, 10)
    c = a * x + b
    return a, b, c, x

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧮")

st.title("🧮 Práctica de Ecuaciones de Primer Grado")

# Estado de sesión para mantener la misma ecuación hasta que se quiera una nueva
if 'a' not in st.session_state:
    st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.solucion = generar_ecuacion()

a = st.session_state.a
b = st.session_state.b
c = st.session_state.c
solucion = st.session_state.solucion

st.markdown("### Resuelve la siguiente ecuación:")
st.latex(f"{a}x + ({b}) = {c}")

respuesta = st.number_input("Tu respuesta para x:", step=1)

if st.button("Verificar"):
    if respuesta == solucion:
        st.success("✅ ¡Correcto!")
    else:
        st.error(f"❌ Incorrecto. La solución correcta es x = {solucion}")

if st.button("Nueva ecuación"):
    st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.solucion = generar_ecuacion()
    st.experimental_rerun()
