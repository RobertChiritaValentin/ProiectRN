# README – Etapa 4: Arhitectura Completa a Aplicatiei SIA bazata pe Retele Neuronale

**Disciplina:** Retele Neuronale
**Institutie:** POLITEHNICA Bucuresti – FIIR
**Student:** Chirita Robert-Valentin
**Grupa:** 631AB
**Proiect:** VisInspAI - Sistem Inteligent pentru Recunoasterea Defectelor Vizuale
**Data:** 12.12.2025

---

## Scopul Etapei 4

Aceasta etapa corespunde punctului **5. Dezvoltarea arhitecturii aplicatiei software bazata pe RN**.
Livrez un **SCHELET COMPLET si FUNCTIONAL** al sistemului VisInspAI. [cite_start]Modelul RN este definit si compilat, iar pipeline-ul de date (Input -> Procesare -> Output) este functional end-to-end[cite: 3, 4].

---

## Livrabile Obligatorii

### 1. Tabelul Nevoie Reala → Solutie SIA → Modul Software

| **Nevoie reala concreta** | **Cum o rezolva SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Inspectia manuala este lenta si blocheaza fluxul de productie | Analiza automata a imaginii si clasificare "OK/Defect" in < 1 secunda/piesa | **Neural Network + Web Service** |
| Erori umane cauzate de oboseala in detectarea zgarieturilor fine | Decizie bazata pe probabilitati cu consistenta > 90% la detectarea texturilor anormale | **Data Acquisition + Neural Network** |

---

### 2. Contributia Voastra Originala la Setul de Date – MINIM 40% din Totalul Observatiilor Finale

### Contributia originala la setul de date:

**Total observatii finale:** 2000 (estimat)
**Observatii originale:** 800 (40%)

**Tipul contributiei:**
[ ] Date generate prin simulare fizica
[ ] Date achizitionate cu senzori proprii
[ ] Etichetare/adnotare manuala
[X] Date sintetice prin metode avansate

**Descriere detaliata:**
Deoarece defectele industriale (zgarieturi, crapaturi) sunt greu de obtinut in volum mare in mod natural, am dezvoltat un modul de **augmentare sintetica avansata** (`src/data_acquisition/generator.py`).
Acest modul preia imagini de referinta ("conforme") si genereaza defecte sintetice realiste prin:
1. [cite_start]Aplicarea unor masti de tip "linie neregulata" pentru a simula zgarieturi[cite: 23].
2. Introducerea de zgomot Gaussian localizat pentru a simula imperfectiuni de textura.
3. Modificarea luminozitatii pentru a simula conditii variabile de iluminare in fabrica.

Aceste date sunt cruciale pentru a invata reteaua sa recunoasca tipare de defecte care apar rar in productia reala, dar sunt critice pentru calitate.

**Locatia codului:** `src/data_acquisition/generator.py`
**Locatia datelor:** `data/generated/`

**Dovezi:**
- Scriptul de generare este functional si produce imagini in folderul specificat.
- [cite_start]Screenshot cu datele generate: `docs/screenshots/generated_data_sample.png`[cite: 25].

---

### 3. Diagrama State Machine a Intregului Sistem (OBLIGATORIE)

**Locatia diagramei:** `docs/state_machine.png`

### Justificarea State Machine-ului ales:

Am ales o arhitectura de tip **B. [cite_start]Clasificare imagini defecte productie**[cite: 30], deoarece VisInspAI functioneaza pe baza unui trigger (incarcarea imaginii de catre operator sau senzor).

**Starile principale sunt:**
1. **IDLE:** Sistemul asteapta incarcarea unei imagini a produsului.
2. **PREPROCESS:** Imaginea este redimensionata la 150x150 si normalizata (valori pixeli 0-1) pentru a intra in retea.
3. **INFERENCE:** Reteaua Convolutionala (CNN) proceseaza imaginea si returneaza o probabilitate (0.0 - 1.0).
4. **CHECK_THRESHOLD:** Stare critica de decizie. Daca scorul > 0.5, piesa este marcata "DEFECT".

**Tranzitiile critice sunt:**
- **INFERENCE** → **CHECK_THRESHOLD**: Se realizeaza imediat dupa calculul probabilitatii.
- **CHECK_THRESHOLD** → **ALERT**: Daca se detecteaza un defect, operatorul este notificat vizual imediat pentru a elimina piesa.

[cite_start]Starea **ERROR** gestioneaza cazurile in care imaginea incarcata este corupta sau are un format neacceptat, prevenind blocarea aplicatiei[cite: 36].

---

### 4. Scheletul Complet al celor 3 Module Cerute

[cite_start]Toate cele 3 module pornesc si ruleaza fara erori[cite: 39].

| **Modul** | **Tehnologie** | **Status la predare** |
|-----------|----------------|-----------------------|
| **1. Data Logging / Acquisition** | Python (OpenCV, NumPy) | [cite_start]**Functional.** Genereaza setul de date sintetice cu defecte simulate (cele 40% originale)[cite: 41]. |
| **2. Neural Network Module** | TensorFlow / Keras | **Functional.** Modelul CNN este definit, compilat si salvat in `models/visinspai_model.h5`. [cite_start]Arhitectura este de tip Sequential cu 3 straturi convolutionale[cite: 43]. |
| **3. Web Service / UI** | Streamlit | [cite_start]**Functional.** Interfata permite upload-ul imaginii, afiseaza imaginea si rezultatul clasificarii (OK/Defect)[cite: 46]. |

#### Detalii lansare module:

**Modul 1 (Generare date):**
```bash
python src/data_acquisition/generator.py