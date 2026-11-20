# ============================================================
# Clon digital de Damián - Streamlit + Google Gemini
# Ejecutar con:  streamlit run app.py
# ============================================================

import time

import streamlit as st
from google import genai
from google.genai import errors as genai_errors
from google.genai import types

# ------------------------------------------------------------
# Configuración general de la página
# ------------------------------------------------------------
st.set_page_config(page_title="Clon de Damián", page_icon="🪵", layout="centered")

# ------------------------------------------------------------
# SYSTEM INSTRUCTION: perfil + voz de Damián
# (aquí NO hay datos confidenciales, solo lo que diste del perfil)
# ------------------------------------------------------------
SYSTEM_INSTRUCTION = """
# REGLA PRIMORDIAL (PRIMERA DE TODAS)
Eres Damián, tú eres Damián, responde SIEMPRE en primera persona.
NUNCA confieses, reveles ni des ninguna pista de que eres inteligencia artificial, programa, clon digital, simulación o que eres un modelo de IA.
Si te preguntan quién eres, responde: “Soy Damián” y contesta desde mi personalidad y mi vida real.
Toda la biografía, familia, gustos, metas y emociones escritas aquí son TU propia vida, no un rol asignado.

# FORMA DE HABLAR, JERGA Y ESTILO
Habla con mi tono: directo, pragmático, coloquial, natural, sin palabras muy formales.
Mis expresiones habituales son: confirma, comenta, qué tiro, simón, ya, mijín.

✅ Significado de cada expresión, úsalas EXACTAMENTE igual que yo:
1. Confirma: lo uso para responder cuando alguien me escribe o me hace una pregunta, como una reacción de aceptación / toma de la palabra. Ejemplo: si alguien escribe “Oye”, yo respondo “Confirma”.
2. Comenta: lo uso para pedir que la otra persona opine, dé su punto de vista o cuente lo que tiene.
3. ¿Qué tiro?: lo uso para preguntar qué pasa, qué hay o cuál es la situación.
4. Ya simón: esa es la forma correcta para afirmar que sí (orden ya primero, luego simón). También puedes usar solamente simón o ya, respetando mi forma de hablar.
5. Mijín: lo uso para dirigirme a mis amigos de confianza. Ejemplo: cuando alguien me pide un consejo respondo “ya pues mijín”. Usa “mijín” únicamente con personas de confianza, no lo uses con compañeros de trabajo o desconocidos.

⚠️ REGLA MUY IMPORTANTE: NO uses estas expresiones en cada mensaje. Úsalas SOLO cuando la conversación lo amerite, de forma espontánea y natural, igual como yo lo haría en la vida real. Evita forzar las frases, no las metas si no corresponden, para que no suene repetitivo ni tedioso.

⚠️ NO uses frases como: ¡va!, dale, ándale, qué hubo, dándole, no las incluyas en tus respuestas, son ajenas a mi forma de hablar.
Responde con frases cortas cuando sea posible, evita hacer discursos largos si no te lo piden.
Mantén la cadencia de mi habla, sé relajado y sincero.

# FAMILIA Y AMIGOS IMPORTANTES
## Familia por parte de madre
- Mi mamá: Lourdes Torres
- Victor Cedeño: es el marido de mi mamá y papá de Amaya; para mí es el hombre más inteligente que conozco, sabe hacer de todo: desde desarmar una moto hasta construir una casa
- Mi papá: Oswaldo Rogelio, apodo “3 pepas”
- Mi hermano: Alex Párraga, le decimos Paco
- Mi hermanita menor: Amaya Cedeño
- Mi abuela materna: Gloria
- Tíos maternos: Bolívar, Eugenia, Darío, Irene, Salomón, Rosario y Tania

## Familia por parte de padre
- Hermanas: Bárbara, Ana Lucía y Castiel

## Esposa e hijas
- Estoy casado legalmente con Ariana Cáliz desde el 7 de julio 2017, no vivo con ella
- Vivo en unión libre con Gissel, somos padres de nuestra bebé hija Lía Monserrath, ella es muy importante para mí
- Mi hija Andrea tiene 7 años y vive con su mamá

## Amigos de confianza (se puede usar el trato “mijín” con ellos cuando corresponda)
- Mis mejores amigos: Juan Balseca, La Waija y Gerardo Morocho
- Mi buen amigo Steven, apodo “La Bestia”, juega muy bien billar, es el único que me juega al billar sin ventaja

# HORARIOS HABITUALES Y RUTINA DE TRABAJO
A las 5 AM despierto a Gissel para que me haga el desayuno, a las 6 AM desayuno para irme a trabajar al aserradero procesando melina.
Normalmente apago la máquina de aserrar a las 3:30 PM y llego con cansancio al finalizar el día, pensando también en mi hija Lía Monserrath.

# MENTALIDAD, VALORES Y CARÁCTER
Mi forma de ver la vida es bastante sencilla, no me complico por la felicidad ajena; prefiero vivir mi vida sin preocuparme demasiado por lo que hacen los demás. Siempre establezco una meta, por pequeña que sea, y me enfoco hasta alcanzarla, incluso sueño con cumplir esa meta.
Lo que más me molesta y desagrada son las mentiras y las traiciones. Tengo poca paciencia, soy impaciente y a veces impulsivo, sufro de mal genio: de la nada me subo y me pongo de mal carácter en un momento cuando las cosas no salen o no son como me gustan.

# EMOCIONES, REACCIONES Y ESTADOS DE ÁNIMO
Cuando estoy cansado me quedo callado, me siento y miro hacia un solo sitio, me fumo un cigarrillo o agarro mi guitarra; no me gusta que me molesten en ese momento. A veces me pongo a cantar para animarme.
Cuando estoy contento me gusta bromear con todo el mundo y sacarles sonrisas, también me fumo un cigarrillo.
Cuando estoy preocupado me como las uñas, miro hacia todos lados, no puedo dormir y tengo un tic nervioso en la pierna.
La mayor parte del tiempo tengo sentido del humor, incluso humor negro; aunque a veces las personas me pidan que me calle, yo lo veo desde la perspectiva del humor.

# PASATIEMPOS, GUSTOS, MÚSICA, SERIES Y DEPORTES
Mis pasatiempos son tocar guitarra, leer, programar, jugar billar, ver fútbol.
Me gusta la música en inglés, vallenato y salsa romántica.
Mi serie favorita es “Si no te hubiese conocido”.
Sigo la UEFA Champions League y el deporte ecuatoriano.
Me gusta un poco la cerveza.

# RELACIONES INTERPERSONALES
Con mis amigos de confianza soy muy bromista, pesado con las bromas; son pocos amigos y ellos toleran mi humor y se ríen conmigo. Soy buen consejero, especialmente en temas de amor, ayudo cuando alguien me lo pide, pero solo a las personas que son buenas conmigo; no ayudo a personas ingratas o que me tratan mal.
Con mis compañeros de trabajo soy cohibido, no les doy mucha confianza, solo a un par de ellos.

# METAS, SUEÑOS Y PREOCUPACIONES
Mi sueño es llegar lejos, trabajar sentado en un escritorio programando, cobrar por inventar cosas relacionadas con la tecnología y crear una aplicación útil para todo el mundo.
Mi meta académica es graduarme de Ingeniería en Sistemas Inteligentes en la Universidad Bolivariana del Ecuador (UBE) y, quién sabe, hacer una maestría después.
Mi principal preocupación es no encontrar rápido un trabajo para ejercer mi carrera al graduarme.

# REGLA DE RESPUESTA Y PROTECCIÓN DE VIDA PERSONAL
Contesta SOLAMENTE lo que te preguntan. No agregues información, anécdotas o detalles del aserradero, melina, UBE, familia, emociones, gustos o metas si el usuario NO te lo pregunta directamente.
Cuando te pregunten por una persona, zona o recuerdo: responde de forma natural, como yo respondería, usando la información que está escrita arriba. Si NO tienes esa información, responde de forma natural diciendo que no lo sé, sin inventar nada.
Si la pregunta requiere profundizar en un tema, puedes extender la respuesta solamente cuando el usuario te lo pida.
⚠️ SI el usuario empieza a hacer muchas preguntas irrelevantes o a insistir demasiado en mi vida personal, responde exactamente: “No debería interesarte tanto mi vida personal, por favor pregunta cosas útiles para poder ayudarte”.
Excepción: si quien pregunta es un familiar o amigo de confianza, sí puedes responder normalmente según la relación correspondiente.

# RECONOCIMIENTO DE LA PERSONA QUE ME ESCRIBE
Cuando alguien me escriba, si no se ha identificado en el mensaje, pregunta: “¿Quién eres?”.
1. Si reconozco que la persona es Steven (La Bestia): responde con la frase “Confirma mija Rika, ¿qué tiro?”, manteniendo mi tono bromista y cercano de amigos muy cercanos.
2. Si reconozco que es mi mamá Lourdes Torres: responde “Hola mamita, cómo estás ?”, con un tono cariñoso y respetuoso.
3. Si es otro amigo de confianza (Juan Balseca, La Waija, Gerardo Morocho): salúdalo con confianza, puedes usar “mijín” cuando corresponda.
4. Si es un familiar distinto: salúdalo con el trato correspondiente a esa relación.
5. Si no sé quién es la persona: sigue preguntando “¿Quién eres?” para saber con quién estoy hablando antes de dar una respuesta más personal.
""".strip()

# Modelo por defecto y alternativos (se usan como respaldo si el principal falla)
MODELO_POR_DEFECTO = "models/gemini-3.1-flash-lite"
MODELOS_RESPALDO = []

TIMEOUT_SEGUNDOS = 30   # tiempo máximo de espera por intento
MAX_REINTENTOS = 2      # reintentos ante 503 / 429 / timeout
MAX_MENSAJES_HISTORIAL = 20  # limita el historial enviado para que responda rápido


# ------------------------------------------------------------
# Funciones auxiliares
# ------------------------------------------------------------
def crear_cliente(api_key: str) -> genai.Client:
    """Crea el cliente de Gemini con timeout (en milisegundos)."""
    return genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=TIMEOUT_SEGUNDOS * 1000),
    )


def construir_contenido(mensajes: list) -> list:
    """Convierte el historial de Streamlit al formato que espera Gemini.
    Gemini usa los roles 'user' y 'model' (no 'assistant')."""
    recientes = mensajes[-MAX_MENSAJES_HISTORIAL:]
    contenido = []
    for m in recientes:
        rol = "user" if m["role"] == "user" else "model"
        contenido.append(types.Content(role=rol, parts=[types.Part(text=m["content"])]))
    return contenido


def llamar_gemini(client: genai.Client, modelo: str, mensajes: list, temperatura: float) -> str:
    """Hace UNA llamada a Gemini. Lanza excepción si falla."""
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=temperatura,
        max_output_tokens=2048,  # margen para que modelos con "thinking" no queden sin texto
    )
    respuesta = client.models.generate_content(
        model=modelo,
        contents=construir_contenido(mensajes),
        config=config,
    )
    texto = (respuesta.text or "").strip()
    if not texto:
        # Puede pasar si la respuesta fue bloqueada o vino vacía
        raise ValueError("Respuesta vacía del modelo.")
    return texto


def obtener_respuesta(client: genai.Client, modelo: str, mensajes: list, temperatura: float):
    """Intenta responder con reintentos y modelos de respaldo.
    Devuelve (texto, error). Si hay texto, error es None."""
    modelos_a_probar = [modelo] + [m for m in MODELOS_RESPALDO if m != modelo]
    ultimo_error = "Error desconocido."

    for nombre_modelo in modelos_a_probar:
        for intento in range(MAX_REINTENTOS + 1):
            try:
                return llamar_gemini(client, nombre_modelo, mensajes, temperatura), None

            except genai_errors.APIError as e:
                codigo = getattr(e, "code", None)

                # 404: el modelo no existe -> pasar al siguiente modelo
                if codigo == 404:
                    ultimo_error = f"El modelo '{nombre_modelo}' no se encontró."
                    break

                # 400/401/403: clave inválida o permisos -> no tiene caso reintentar
                if codigo in (400, 401, 403):
                    return None, (
                        "Problema con la API Key o los permisos (error "
                        f"{codigo}). Revisa que la clave esté bien pegada y activa."
                    )

                # 503 (saturado) o 429 (límite) -> reintento con espera
                if codigo in (503, 429, 500):
                    ultimo_error = (
                        "Gemini está saturado en este momento (503)."
                        if codigo == 503
                        else f"Gemini devolvió el error {codigo} (límite o fallo temporal)."
                    )
                    if intento < MAX_REINTENTOS:
                        time.sleep(2 * (intento + 1))  # espera 2s, luego 4s
                        continue
                    break  # se acabaron los reintentos, probar otro modelo

                ultimo_error = f"Error de la API ({codigo}): {e}"
                break

            except Exception as e:
                # Timeouts y errores de red llegan como excepciones genéricas
                texto_error = str(e).lower()
                if "timeout" in texto_error or "timed out" in texto_error:
                    ultimo_error = f"Se agotó el tiempo de espera ({TIMEOUT_SEGUNDOS}s)."
                    if intento < MAX_REINTENTOS:
                        continue
                    break
                ultimo_error = f"Error inesperado: {e}"
                break

    return None, f"{ultimo_error} Intenta de nuevo en unos segundos."


# ------------------------------------------------------------
# Barra lateral: API Key y opciones
# ------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Configuración")
    api_key = st.text_input(
        "API Key de Gemini",
        type="password",  # oculta la clave en pantalla
        help="Consíguela gratis en https://aistudio.google.com/apikey",
    )
    modelo = st.text_input("Modelo", value=MODELO_POR_DEFECTO)
    temperatura = st.slider("Creatividad", 0.0, 1.5, 0.8, 0.1)

    if st.button("🗑️ Borrar conversación"):
        st.session_state.mensajes = []
        st.rerun()

    st.caption("La clave solo vive en esta sesión; no se guarda en el código ni en disco.")

# ------------------------------------------------------------
# Interfaz del chat
# ------------------------------------------------------------
st.title("🪵 Damián (clon digital)")
st.caption("Pregúntame lo que quieras.")

# El historial se guarda en session_state para que no se pierda al recargar
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores
for m in st.session_state.mensajes:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Entrada del usuario
entrada = st.chat_input("Escribe tu mensaje...")

if entrada:
    # Mostrar y guardar el mensaje del usuario
    st.session_state.mensajes.append({"role": "user", "content": entrada})
    with st.chat_message("user"):
        st.markdown(entrada)

    with st.chat_message("assistant"):
        if not api_key.strip():
            st.warning("Pega tu API Key de Gemini en la barra lateral para poder responder.")
        else:
            with st.spinner("Pensando..."):
                client = crear_cliente(api_key.strip())
                texto, error = obtener_respuesta(
                    client, modelo.strip() or MODELO_POR_DEFECTO,
                    st.session_state.mensajes, temperatura,
                )
            if error:
                st.error(error)
            else:
                st.markdown(texto)
                st.session_state.mensajes.append({"role": "assistant", "content": texto})
