# 📘 README – Etapa 5: Antrenarea Modelului RN

**Student:** Chirita Robert-Valentin
**Grupa:** 631AB
**Proiect:** VisInspAI - Detectie Defecte Industriale

---

## 1. Descriere
In aceasta etapa am realizat antrenarea retelei neuronale convolutionale (CNN) pentru clasificarea defectelor in 6 categorii (Crazing, Inclusion, Patches, Pitted, Rolled, Scratches).

## 2. Configurarea Antrenarii
Antrenarea a fost realizata in cloud (Google Colab) pentru a beneficia de GPU, folosind setul de date procesat in etapele anterioare.

| Hiperparametru | Valoare | Justificare |
|----------------|---------|-------------|
| **Arhitectura**| CNN Custom (3 layere Conv2D) | Suficienta pentru extragerea trasaturilor de textura (defecte). |
| **Input Size** | 150x150 px | Compromis bun intre detaliu vizual si viteza de procesare. |
| **Batch Size** | 32 | Standard pentru stabilitatea gradientului. |
| **Epoci** | 15 | Convergenta atinsa rapid, fara overfitting major. |
| **Loss** | Categorical Crossentropy | Problema Multi-Class (6 clase). |
| **Optimizer** | Adam | Convergenta rapida si adaptiva. |

## 3. Rezultate
Modelul antrenat a fost salvat in `models/trained_model.h5`.

- **Grafice:** Curbele de invatare (Loss/Accuracy) se gasesc in `docs/loss_curve.png`.
- **Matricea de Confuzie:** Performanta pe fiecare clasa este vizibila in `docs/confusion_matrix.png`.
- **Istoric:** Log-urile detaliate sunt in `results/training_history.csv`.

## 4. Integrare
Modelul a fost integrat in aplicatia Streamlit (`src/app/app.py`).
Dovada functionarii (inferenta pe o imagine noua) se gaseste in `docs/screenshots/inference_real.png`.