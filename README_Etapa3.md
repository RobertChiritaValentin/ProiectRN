# Sistem Inteligent pentru Recunoasterea Defectelor Vizuale in Produse

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Chirita Robert-Valentin 
**Data:** 20.11.2025

##  1. Structura Repository-ului Github 

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
│   └── datasets/				   # Documentatie dataset
│       └── readme.md
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

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** imagini colectate manual de pe internet din surse publice
* **Modul de achiziție:** Gratis
* **Perioada / condițiile colectării:** Noiembrie 2025 // Descare de pe website

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 1400
* **Tipuri de date:** ☐ Imagini
* **Format fișiere:** ☐ JPG / ☐ XML

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
|-------------------|---------|-------------|---------------|--------------------|
| imagine | matricial |  | [1500] | imagine RGB convertita la 150x150 greyscale |
| label | categorial | | | {defect,nedefect}

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

Dimensiuni variate initial
Contrast neuniform - rezolvat la preprocesare
Diferențe mari de iluminare

### 3.2 Analiza calității datelor

	Nicio imagine coruptă
	Necesitate transformare în grayscale + reducere noise

### 3.3 Probleme identificate

	 iluminare neuniformă - contrast adjustment
	 unele imagini prea mari - resize 150×150
	 variații vizibile de orientare fisuri - augmentare cu rotații
---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

Eliminare imagini duble
Eliminare imagini neclare
Conversie grayscale
Resize 150×150 px


### 4.2 Transformarea caracteristicilor

Normalizare
Noise reduction

### 4.3 Structurarea seturilor de date

* 70% – train
* 15% – validation
* 15% – test

### 4.4 Salvarea rezultatelor preprocesării

	imagini procesate în data/processed/
	structurate pe clase în train/val/test/

---

##  5. Fișiere Generate în Această Etapă

data/raw/ – imaginile brute
data/processed/ – grayscale + resize 150x150
@resize.py – script complet în Python pentru procesare imagini
@datasplit.py - imparte imaginile procesate automat in test, train, val in proportii 70/15/15

---

##  6. Stare Etapă (de completat de student)

- [x] Structură repository configurată
- [x] Dataset analizat (EDA realizată)
- [x] Date preprocesate
- [x] Seturi train/val/test generate
- [x] Documentație actualizată în README + `data/README.md`


---
