import streamlit as st

st.title("🌍 Explorador de Decisiones – Juego Gamificado")
st.write("Responde las preguntas y descubrí tu perfil.\n")

puntajes = {"Innovador":0, "Estratégico":0, "Colaborativo":0, "Audaz":0}

# Pregunta 1
resp1 = st.radio("1️⃣ El río caudaloso: Tenés que cruzar un río. ¿Qué hacés?",
                 ["Construís una balsa improvisada",
                  "Buscás un puente más adelante",
                  "Pedís ayuda a otros viajeros"])
if resp1 == "Construís una balsa improvisada": puntajes["Innovador"] += 1
elif resp1 == "Buscás un puente más adelante": puntajes["Estratégico"] += 1
else: puntajes["Colaborativo"] += 1

# Pregunta 2
resp2 = st.radio("2️⃣ El camino oscuro: El sendero se divide en dos.",
                 ["Elegís el iluminado (seguro)",
                  "Elegís el oscuro (riesgoso)",
                  "Esperás más información"])
if resp2 == "Elegís el iluminado (seguro)": puntajes["Estratégico"] += 1
elif resp2 == "Elegís el oscuro (riesgoso)": puntajes["Audaz"] += 1
else: puntajes["Estratégico"] += 1

# Pregunta 3
resp3 = st.radio("3️⃣ El cofre misterioso: Encontrás un cofre cerrado.",
                 ["Intentás abrirlo con ingenio",
                  "Lo dejás y seguís",
                  "Lo marcás para volver después"])
if resp3 == "Intentás abrirlo con ingenio": puntajes["Innovador"] += 1
elif resp3 == "Lo dejás y seguís": puntajes["Audaz"] += 1
else: puntajes["Estratégico"] += 1

# Pregunta 4
resp4 = st.radio("4️⃣ El cruce final: Llegás a una montaña que bloquea tu paso.",
                 ["Escalás directamente",
                  "Buscás un camino alternativo",
                  "Esperás ayuda externa"])
if resp4 == "Escalás directamente": puntajes["Audaz"] += 1
elif resp4 == "Buscás un camino alternativo": puntajes["Estratégico"] += 1
else: puntajes["Colaborativo"] += 1

# Resultado final
if st.button("Ver mi perfil"):
    perfil = max(puntajes, key=puntajes.get)
    st.success(f"🎉 Tu perfil es: {perfil}")
    if perfil == "Innovador":
        st.write("👉 Sos creativo/a y resolutivo/a, buscás soluciones originales.")
    elif perfil == "Estratégico":
        st.write("👉 Sos analítico/a y planificador/a, pensás en el largo plazo.")
    elif perfil == "Colaborativo":
        st.write("👉 Valorás el trabajo en equipo y la comunicación.")
    elif perfil == "Audaz":
        st.write("👉 Te adaptás rápido y tomás riesgos con confianza.")
