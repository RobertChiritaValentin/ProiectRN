# README – Etapa 4: Arhitectura Completa a Aplicatiei SIA bazata pe Retele Neuronale

**Disciplina:** Retele Neuronale
**Institutie:** POLITEHNICA Bucuresti – FIIR
**Student:** Chirita Robert-Valentin
**Grupa:** 631AB
**Proiect:** VisInspAI - Sistem Inteligent pentru Recunoasterea Defectelor Vizuale
**Data:** 12.12.2025

---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

## Livrabile Obligatorii

### 1. Tabelul Nevoie Reala → Solutie SIA → Modul Software

| **Nevoie reala concreta** | **Cum o rezolva SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Inspectia manuala este lenta si blocheaza fluxul de productie | Analiza automata a imaginii si clasificare "OK/Defect" in < 1 secunda/piesa | **Neural Network + Web Service** |
| Erori umane  in detectarea zgarieturilor fine | Decizie bazata pe probabilitati cu consistenta > 90% la detectarea texturilor anormale | **Data Acquisition + Neural Network** |

---

### 2. Contributia Voastra Originala la Setul de Date – MINIM 40% din Totalul Observatiilor Finale

### Contributia originala la setul de date:

**Total observatii finale:** 1400

**Tipul contributiei:**
[ ] Date generate prin simulare fizica
[ ] Date achizitionate cu senzori proprii
[ ] Etichetare/adnotare manuala
[X] Date sintetice prin metode avansate

**Descriere detaliata:**
Deoarece defectele industriale (zgarieturi, crapaturi) sunt greu de obtinut in volum mare in mod normal am dezvoltat un modul de **augmentare sintetica avansata** (`src/data_acquisition/generator.py`).
Acest modul preia imagini de referinta ("conforme") si genereaza defecte sintetice realiste prin:
1. Aplicarea unor masti de tip "linie neregulata" pentru a simula zgarieturi.
2. Introducerea de zgomot Gaussian localizat pentru a simula imperfectiuni de textura.
3. Modificarea luminozitatii pentru a simula conditii variabile de iluminare in fabrica.

Aceste date sunt cruciale pentru a invata reteaua sa recunoasca tipare de defecte care apar rar in productia reala, dar sunt critice pentru calitate.

**Locatia codului:** `src/data_acquisition/generator.py`
**Locatia datelor:** `data/generated/`

**Dovezi:**
- Scriptul de generare este functional si produce imagini in folderul specificat.
- Screenshot cu datele generate: `docs/screenshots/generated_data_sample.png`

---

### 3. Diagrama State Machine a Intregului Sistem (OBLIGATORIE)

**Locatia diagramei:** `docs/state_machine.png`

### Justificarea State Machine-ului ales:

Am ales o arhitectura de tip **B. Clasificare imagini defecte productie**, deoarece VisInspAI functioneaza pe baza unui trigger (incarcarea imaginii de catre operator sau senzor).

**Starile principale sunt:**
1. **IDLE:** Sistemul asteapta incarcarea unei imagini a produsului.
2. **PREPROCESS:** Imaginea este redimensionata la 150x150 si normalizata (valori pixeli 0-1) pentru a intra in retea.
3. **INFERENCE:** Reteaua Convolutionala (CNN) proceseaza imaginea si returneaza o probabilitate (0.0 - 1.0).
4. **CHECK_THRESHOLD:** Stare critica de decizie. Daca scorul > 0.5, piesa este marcata "DEFECT".

**Tranzitiile critice sunt:**
- **INFERENCE** → **CHECK_THRESHOLD**: Se realizeaza imediat dupa calculul probabilitatii.
- **CHECK_THRESHOLD** → **ALERT**: Daca se detecteaza un defect, operatorul este notificat vizual imediat pentru a elimina piesa.

Starea **ERROR** gestioneaza cazurile in care imaginea incarcata este corupta sau are un format neacceptat, prevenind blocarea aplicatiei.

---

### 4. Scheletul Complet al celor 3 Module Cerute

Toate cele 3 module pornesc si ruleaza fara erori.

| **Modul** | **Tehnologie** | **Status la predare** |
|-----------|----------------|-----------------------|
| **1. Data Logging / Acquisition** | Python (OpenCV, NumPy) | **Functional.** Genereaza setul de date sintetice cu defecte simulate (cele 40% originale). |
| **2. Neural Network Module** | TensorFlow / Keras | **Functional.** Modelul CNN este definit, compilat si salvat in `models/visinspai_model.h5`. [cite_start]Arhitectura este de tip Sequential cu 3 straturi convolutionale. |
| **3. Web Service / UI** | Streamlit | **Functional.** Interfata permite upload-ul imaginii, afiseaza imaginea si rezultatul clasificarii (OK/Defect). |

## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
ProiectRN/
├── README.md                      # Descriere proiect
├── START_VISINSPAI.command        # Script pornire MacOS 
├── START_WINDOWS.bat              # Script pornire Windows
├── requirements.txt               # Lista biblioteci
│
├── config/                        # Configurari globale
│   └── settings.json              # Definire cai
│
├── data/                          # Seturi de date
│   ├── generated/                 # Imagini generate de min
│   ├── raw/                       # Imagini brute pe categorii (Crazing, Inclusion, etc)
│   ├── processed/                 # Imagini redimensionate la 150x150 si Greyscale
│   ├── train/                     # Setul de date pentru antrenarea retelei (70%)
│   ├── validation/                # Setul de date pentru validarea performantei (15%)
│   └── test/                      # Imagini testare live in timpul prezentarii (15%)
│
├── docs/                          # Documentatie aditionala
│   └── screenshots/
│       ├── loss_curve.png         # Grafic de antrenare
│       ├── confusion_matrix.png   # Matricea de confuzie initiala
│       └── confusion_matrix_optimized.png # Rezultatul modelului optimizat
│
├── models/                        # Modelele salvate
│   └── optimized_model.h5         # Modelul final optimizat
│   └── trained_model.h5           # Model intermediar
│   └── visinspai_model.h5         # Primul model
│
├── reports/                       # Rapoarte si analize vizuale
│   └── figures/
│       ├── accuracy_plot.png      # Evolutia acuratetei (atinge ~96%)
│       ├── loss_plot.png          # Scaderea erorii pe parcursul celor 15 epoci
│       └── experiments_comparison.png # Comparatia intre variantele de arhitectura
│
├── results/                       # Date brute din experimente
│   ├── training_history.csv       # Valorile acuratetei si pierderii salvate
│   └── optimization_experiments.csv # Rezultatele testelor pentru Baseline vs. Dropout
│
└── src/                           # Cod sursa
    ├── app/
    │   └── app.py                 # Streamlit app
    ├── data_acquisition/
    │   └── generator.py           # Date generate de mine
    ├── neural_network/            # Implementare retea
    │   ├── evaluate.py            # Testare (Confusion Matrix)
    │   ├── model.py               # Definire arhitectura CNN
    │   └── train.py               # Antrenare, salvare si plotare
    └── preprocessing/             # Scripturi pentru prelucrare
        ├── @datasplit.py          # Impartire in test/train/validation 70/15/15
        ├── @generateplots.py      # Generare grafice
        ├── @okimage.py            # Generare iagine suprafata ok
        └── @resize.py             # Redimensionare dataset si greyscale
```

#### Detalii lansare module:

**Modul 1 (Generare date):**
```bash
python src/data_acquisition/generator.py