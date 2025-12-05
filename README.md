# Sistem Inteligent pentru Recunoasterea Defectelor Vizuale in Produse

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Chirita Robert-Valentin 
**Data:** 20.11.2025

##  1. Structura Repository-ului Github 

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** imagini colectate manual de pe internet din surse publice
* **Modul de achiziție:** Gratis
* **Perioada / condițiile colectării:** Noiembrie 2025 // Descare de pe website

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 1500
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

Dimensiuni variate inițial (480–1920 px)
Contrast neuniform → rezolvat la preprocesare
Diferențe mari de iluminare

### 3.2 Analiza calității datelor

	Nicio imagine coruptă
	~2% imagini neclare / subexpuse → eliminate
	Necesitate transformare în grayscale + reducere noise

### 3.3 Probleme identificate

	⚠ iluminare neuniformă → contrast adjustment
	⚠ unele imagini prea mari → resize 150×150
	⚠ variații vizibile de orientare fisuri → augmentare cu rotații
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
	parametrii de preprocesare salvați în config/preprocess.yaml

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
