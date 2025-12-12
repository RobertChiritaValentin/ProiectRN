import streamlit as st
import numpy as np
from PIL import Image
import time
import random

# config pagina
st.set_page_config(
    page_title="VisInspAI - Demo",
    page_icon="〄",
    layout="centered"
)

# titlu header
st.title("VisInspAI - Detectie Defecte")
st.markdown("### Sistem Inteligent pentru Controlul Calitatii Vizuale")
st.info("Versiune Schelet Functional - Etapa 4 (Model Neantrenat / Demo)")

# MOCK MODEL - Simulam incarcarea modelului pentru a evita crash-ul pe macOS
# Nu mai importam tensorflow aici pentru ca inchide scriptul instant
model = "DEMO_MODE"

#interfata
#upload
st.divider()
uploaded_file = st.file_uploader("Incarca imaginea piesei pentru inspectie:", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    #imagine incarcata
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagine Piesa', use_container_width=True)
    
    #buton verficare
    st.divider()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_btn = st.button("Analizeaza Piesa", type="primary", use_container_width=True)

    if analyze_btn:
        with st.spinner('Procesare imagine cu Reteaua Neuronala...'):
            #intarziere simulare procesare
            time.sleep(1.5)
            
            #logica predictie SIMULATA
            #Generam un scor random deoarece suntem in Etapa 4 (Schelet)
            #si vrem sa evitam eroarea de driver video/tensorflow
            score = random.random()

            # rezultate
            st.divider()
            st.subheader("Rezultatul Analizei:")
            
            st.progress(int(score * 100), text=f"Probabilitate Defect: {score:.2%}")
            
            if score >= 0.5:
                st.error("REZULTAT: DEFECT DETECTAT")
                st.write("**Actiune recomandata:** Respingere piesa si verificare manuala.")
            else:
                st.success("REZULTAT: PIESA OK")
                st.write("**Actiune recomandata:** Validare si trimitere la ambalare.")