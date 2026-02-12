import streamlit as st
import numpy as np
from PIL import Image
import os
import time
import tensorflow as tf

# configuram pagina aplicatiei cu titlu si layout
st.set_page_config(page_title="VisInspAI - Optimized", page_icon="🚀", layout="centered")
# afisam titlul principal al aplicatiei
st.title("🏭 VisInspAI - Versiune Optimizată (Etapa 6)")
st.markdown("### Sistem Avansat de Control Calitate")

# definim numele claselor de defecte posibile in ordinea antrenarii
CLASS_NAMES = ['Crazing', 'Inclusion', 'Patches', 'Pitted', 'Rolled', 'Scratches']

# functia care incarca modelul real antrenat
@st.cache_resource
def load_model():
    # construim calea catre fisierul modelului
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, '../../models/optimized_model.h5')
    
    # verificam daca fisierul exista fizic pe disc
    if not os.path.exists(model_path):
        return None
    
    # incarcam modelul keras complet
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Eroare la incarcarea modelului: {e}")
        return None

# incercam sa incarcam modelul
model = load_model()

# verificam starea modelului si afisam mesaj corespunzator
if model is None:
    st.error("⚠️ Modelul 'models/optimized_model.h5' lipsește sau este corupt!")
else:
    st.success("✅ Model Optimizat Încărcat și Pregătit pentru Inferență Reală")

# componenta pentru incarcarea imaginii de catre utilizator
uploaded_file = st.file_uploader("Încarcă imaginea piesei:", type=["jpg", "png", "jpeg", "bmp"])

# daca avem o imagine incarcata si modelul e prezent
if uploaded_file is not None and model is not None:
    # deschidem si afisam imaginea pentru confirmare
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Imaginea Încărcată', width=300)
    
    # butonul care declanseaza analiza
    if st.button("🔍 Analiză Detaliată"):
        # afisam un spinner cat timp se proceseaza
        with st.spinner('Procesare imagine cu modelul neuronal...'):
            
            # masuram timpul de start pentru a calcula latenta
            start_time = time.time()
            
            # --- preprocesare imagine pentru model ---
            # redimensionam la 150x150 exact cum a fost antrenat modelul
            img_resized = image.resize((150, 150))
            
            # convertim in array numpy
            img_array = np.array(img_resized)
            
            # normalizam valorile pixelilor la intervalul 0-1
            img_array = img_array / 255.0
            
            # adaugam dimensiunea batch-ului (devine 1, 150, 150, 3)
            img_batch = np.expand_dims(img_array, axis=0)
            
            # --- inferenta reala ---
            # modelul returneaza un array de probabilitati pentru cele 6 clase
            predictions = model.predict(img_batch)
            
            # calculam cat a durat inferenta
            end_time = time.time()
            latency = (end_time - start_time) * 1000
            
            # extragem probabilitatile sub forma de lista simpla
            probs = predictions[0]
            
            # gasim indexul clasei cu cea mai mare probabilitate
            idx = np.argmax(probs)
            confidence = float(probs[idx])
            defect_name = CLASS_NAMES[idx]
            
            st.divider()
            
            # afisam metricile principale pe coloane
            col1, col2 = st.columns(2)
            col1.metric("Defect Identificat", defect_name)
            col2.metric("Latență Inferență", f"{latency:.1f} ms")
            
            # afisam bara de progres pentru incredere
            st.write(f"### Nivel de Încredere: {confidence:.2%}")
            st.progress(int(confidence * 100))
            
            # logica de decizie industriala
            if confidence > 0.75:
                st.error(f"🔴 ACȚIUNE: Piesa RESPINSĂ - Defect {defect_name} detectat cu certitudine mare.")
            elif confidence > 0.45:
                st.warning(f"🟠 ACȚIUNE: Necesită inspecție manuală (Incertitudine la {defect_name}).")
            else:
                # daca nicio clasa nu are scor mare, modelul este confuz
                # in context industrial, daca nu seamana cu niciun defect, e probabil buna
                st.success(f"✅ ACȚIUNE: Piesă CONFORMĂ (Nu s-au detectat defecte evidente).")

            # sectiune expandabila pentru a vedea toate scorurile
            with st.expander("Vezi probabilitățile detaliate (Debug)"):
                # cream un dictionar pentru sortare
                results = {CLASS_NAMES[i]: float(probs[i]) for i in range(len(CLASS_NAMES))}
                # sortam descrescator dupa probabilitate
                sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
                
                for name, score in sorted_results.items():
                    st.write(f"**{name}**: {score:.4f}")
