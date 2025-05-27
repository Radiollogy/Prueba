import streamlit as st

st.set_page_config(page_title="Quiz de Python", page_icon="🐍")

st.title("🐍 Quiz de Python: Repaso de Sintaxis")

st.markdown("### Marca la alternativa correcta para cada pregunta:")

# Preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Cuál es la forma correcta de definir una función en Python?",
        "opciones": [
            "function mi_funcion():",
            "def mi_funcion():",
            "define mi_funcion():",
            "func mi_funcion():"
        ],
        "respuesta": "def mi_funcion():"
    },
    {
        "pregunta": "¿Cuál de las siguientes crea una lista con los números del 1 al 5?",
        "opciones": [
            "[1,2,3,4,5]",
            "list(1 to 5)",
            "{1,2,3,4,5}",
            "(1,2,3,4,5)"
        ],
        "respuesta": "[1,2,3,4,5]"
    },
    {
        "pregunta": "¿Qué hace este código?\n\n```python\nfor i in range(3):\n    print(i)\n```",
        "opciones": [
            "Imprime 1 2 3",
            "Imprime 0 1 2",
            "Imprime 0 1 2 3",
            "Error de sintaxis"
        ],
        "respuesta": "Imprime 0 1 2"
    },
    {
        "pregunta": "¿Cuál es la sintaxis correcta de una instrucción if?",
        "opciones": [
            "if x > 0 then:",
            "if x > 0:",
            "if x > 0 then do:",
            "if (x > 0)"
        ],
        "respuesta": "if x > 0:"
    },
    {
        "pregunta": "¿Cómo se accede al segundo elemento de la lista `mi_lista = ['a', 'b', 'c']`?",
        "opciones": [
            "mi_lista[2]",
            "mi_lista(1)",
            "mi_lista[1]",
            "mi_lista{1}"
        ],
        "respuesta": "mi_lista[1]"
    }
]

# Crear respuestas del usuario
respuestas_usuario = []

# Mostrar las preguntas
for idx, item in enumerate(preguntas):
    st.markdown(f"**{idx + 1}. {item['pregunta']}**")
    respuesta = st.radio(
        label="",
        options=item["opciones"],
        key=f"pregunta_{idx}"
    )
    respuestas_usuario.append(respuesta)

# Botón para verificar respuestas
if st.button("Verificar respuestas"):
    puntaje = 0
    for i in range(len(preguntas)):
        if respuestas_usuario[i] == preguntas[i]["respuesta"]:
            puntaje += 1

    st.markdown(f"### Tu puntaje: **{puntaje} / {len(preguntas)}**")

    if puntaje == len(preguntas):
        st.balloons()
        st.success("¡Excelente! Obtuviste el puntaje perfecto 🎉")
    elif puntaje >= 3:
        st.info("¡Buen trabajo! Sigue practicando 💪")
    else:
        st.warning("Sigue repasando. ¡Tú puedes!")

