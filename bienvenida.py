import streamlit as st

# Configuración de la página (esto pone el icono en la pestaña del navegador)
st.set_page_config(page_title="Consultoría IA", page_icon="🤖")

# Título profesional con icono
st.markdown("<h1 style='text-align: center;'>🏢 Bienvenida al Mundo de la IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Transformando empresas con tecnología inteligente</p>", unsafe_allow_html=True)

st.divider() # Una línea elegante para separar

# Creamos 3 columnas para que los formularios queden alineados
col1, col2, col3 = st.columns(3)

with col1:
    nombre = st.text_input("👤 Tu Nombre", placeholder="Ej: Yvett")

with col2:
    empresa = st.text_input("🏢 Empresa", placeholder="Ej: Innova IA")

with col3:
    sector = st.text_input("📂 Sector", placeholder="Ej: Recursos Humanos")

# Botón centrado y estilizado
st.write("---")
if st.button("🚀 Registrar y Generar Consejo", use_container_width=True):
    if nombre and empresa and sector:
        st.success(f"¡Genial {nombre}! Hemos registrado a **{empresa}** correctamente.")
        
        # Caja de consejo profesional
        with st.container():
            st.info(f"💡 **Consejo de IA para {sector}:** La automatización de procesos en este sector puede reducir tus tareas repetitivas en un 40%. ¡Es el momento de empezar!")
    else:
        st.warning("⚠️ Por favor, completa todos los campos para continuar.")
        