# README – Etapa 6: Analiza Performantei, Optimizarea si Concluzii Finale

**Disciplina:** Retele Neuronale  
**Institutie:** POLITEHNICA Bucuresti – FIIR  
**Student:** Chirita Robert-Valentin
**Link Repository GitHub:** (https://github.com/RobertChiritaValentin/ProiectRN)
**Data predarii:** 15.01.2026

---

## Scopul Etapei 6

Aceasta etapa corespunde punctelor **7. Analiza performantei si optimizarea parametrilor**, **8. Analiza si agregarea rezultatelor** si **9. Formularea concluziilor finale** din lista de 9 etape.

**Obiectiv principal:** Maturizarea completa a Sistemului cu Inteligenta Artificiala (SIA) prin optimizarea modelului RN, analiza detaliata a performantei si integrarea imbunatatirilor in aplicatia software completa.

**CONTEXT:** Aceasta este **ULTIMA VERSIUNE inainte de examen**. Proiectul este acum COMPLET si FUNCTIONAL.

---

## PREREQUISITE – Verificare Etapa 5 (OBLIGATORIU)

- [X] **Model antrenat** salvat in `models/trained_model.h5`
- [X] **Metrici baseline** raportate: Accuracy aprox. 72%
- [X] **UI functional** care incarca modelul antrenat (versiune Cloud/Local)
- [X] **Screenshot inferenta** in `docs/screenshots/inference_real.png`

---

## 1. Actualizarea Aplicatiei Software in Etapa 6 

In aceasta etapa, am trecut de la un prototip functional la o aplicatie optimizata pentru utilizare industriala, capabila sa ofere detalii despre latenta si increderea predictiei.

### Tabel Modificari Aplicatie Software

| **Componenta** | **Stare Etapa 5** | **Modificare Etapa 6** | **Justificare** |
|----------------|-------------------|------------------------|-----------------|
| **Model incarcat** | `trained_model.h5` (Baseline) | `optimized_model.h5` (Deep CNN) | Acuratete crescuta cu 9% si reducere False Negatives. |
| **Afisare UI** | Doar Clasa (Text simplu) | Clasa + Bara Incredere + Latenta | Operatorul uman are nevoie de transparenta pentru decizie. |
| **Logica Decizie** | Binary (OK/Defect) | Multi-Class (6 tipuri) + Status | Diferentiere intre defecte critice (Crazing) si superficiale. |
| **Latenta** | Nemonitorizata | Monitorizata (afisata in ms) | Verificare incadrare in timp real (sub 50ms). |
| **Tratare Erori** | Crash la lipsa model | Fallback elegant + Mesaje eroare | Robustete pentru mediul de productie. |

---

## 2. Analiza Detaliata a Performantei

### 2.1 Confusion Matrix si Interpretare

**Locatie:** `docs/confusion_matrix_optimized.png`

**Interpretare Confusion Matrix:**

**Clasa cu cea mai buna performanta:** `Scratches (Zgarieturi)`
- **Precision:** 92%
- **Recall:** 89%
- **Explicatie:** Zgarieturile au trasaturi vizuale foarte distincte (linii subtiri, contrast mare fata de fundal), fiind usor de detectat de filtrele convolutionale.

**Clasa cu cea mai slaba performanta:** `Rolled-in Scale`
- **Precision:** 68%
- **Recall:** 71%
- **Explicatie:** Aceasta clasa se confunda des cu `Pitted Surface` sau cu fundalul zgomotos, deoarece textura este neregulata si nu are margini clare.

**Confuzii principale:**
1. **Rolled-in Scale** confundat cu **Pitted Surface** in 15% din cazuri.
   - **Cauza:** Ambele defecte reprezinta neregularitati de suprafata; diferenta vizuala este subtila la rezolutia 150x150.
   - **Impact industrial:** Acceptabil, ambele necesita re-prelucrare similara (slefuire).

---

### 2.2 Analiza Detaliata a 5 Exemple Gresite

Am selectat 5 cazuri din setul de test unde modelul a gresit predictia:

| **Index** | **True Label** | **Predicted** | **Confidence** | **Cauza probabila** | **Solutie propusa** |
|-----------|----------------|---------------|----------------|---------------------|---------------------|
| #42 | Scratches | Crazing | 0.55 | Zgarieturi multiple, fine, care seamana cu o retea de crapaturi. | Augmentare cu "Fine Scratches" si rezolutie mai mare. |
| #115 | Patches | Inclusion | 0.48 | Iluminare slaba, pata a parut ca un obiect strain intunecat. | Normalizare histograma (CLAHE) in preprocesare. |
| #203 | Pitted | Rolled-in | 0.61 | Textura foarte similara, confuzie intre clase "vecine". | Colectare mai multe date specifice pentru diferentiere. |
| #330 | Scratches | OK (Noise) | 0.32 | Zgarietura foarte fina, pierduta la resize 150x150. | Input size 224x224 sau cropping inteligent. |
| #512 | Inclusion | Patches | 0.58 | Reflexie puternica a luminii pe incluziune. | Augmentare cu variatii de luminozitate si contrast. |

---

## 3. Optimizarea Parametrilor si Experimentare

### 3.1 Strategia de Optimizare

**Abordare:** Am folosit antrenare in Cloud (Google Colab) pentru a depasi limitarile hardware locale (Mac M1 TensorFlow issues). Am testat manual 4 configuratii distincte.

**Axe de optimizare:**
1. **Learning Rate:** Ajustare pentru convergenta stabila.
2. **Regularizare:** Adaugare Dropout pentru a preveni overfitting-ul observat in Etapa 5.
3. **Arhitectura:** Cresterea adancimii retelei (mai multe straturi Conv2D) pentru extragerea trasaturilor complexe.

### 3.2 Tabel Experimente de Optimizare

| **Exp#** | **Modificare fata de Baseline** | **Accuracy** | **F1-score** | **Observatii** |
|----------|------------------------------------------|--------------|--------------|----------------|
| Baseline | Configuratia din Etapa 5 (Simpla) | 0.72 | 0.68 | Model functional, dar overfitting rapid. |
| Exp 1 | Learning rate 0.001 -> 0.0001 | 0.69 | 0.65 | Convergenta prea lenta, s-a oprit prematur (Early Stopping). |
| Exp 2 | Adaugare Dropout 0.5 | 0.76 | 0.73 | Reducere semnificativa a overfitting-ului. |
| **Exp 3** | **+1 Strat Conv2D (128 filters) + Dropout** | **0.81** | **0.77** | **BEST RESULT.** Balans optim intre complexitate si generalizare. |
| Exp 4 | Batch Size 32 -> 64 | 0.79 | 0.75 | Antrenare mai rapida, dar acuratete usor scazuta. |

**Justificare alegere configuratie finala (Exp 3):**
Am ales **Exp 3** ca model final (`optimized_model.h5`) deoarece a oferit cel mai bun F1-score (0.77), esential intr-un mediu industrial unde vrem sa minimizam atat alarmele false, cat si defectele scapate. Adaugarea stratului suplimentar a permis modelului sa invete texturi mai fine.

---

## 4. Agregarea Rezultatelor Finale

| **Metrica** | **Etapa 4 (Schelet)** | **Etapa 5 (Baseline)** | **Etapa 6 (Optimizat)** | **Target** | **Status** |
|-------------|-------------|-------------|-------------|------------|------------|
| Accuracy | aprox. 16% (Random) | 72% | **81%** | >=80% | ATINS |
| F1-score | aprox. 0.15 | 0.68 | **0.77** | >=0.75 | ATINS |
| Latenta | N/A | aprox. 48ms | **aprox. 35ms** | <=50ms | ATINS |
| False Negatives | N/A | 12% | **5%** | <=5% | ATINS |

---

## 5. Concluzii Finale si Lectii Invatate

### 5.1 Evaluarea Performantei Finale
Proiectul VisInspAI a reusit sa atinga obiectivele propuse, livrand un sistem functional de inspectie vizuala bazat pe CNN. Modelul final clasifica corect 6 tipuri de defecte cu o acuratete de 81%, suficienta pentru un prototip industrial de nivel TRL 4 (Tech Readiness Level).

### 5.2 Limitari Identificate
1. **Hardware Local:** Dezvoltarea pe macOS cu cipuri Apple Silicon a prezentat provocari majore cu bibliotecile TensorFlow (erori mutex), necesitand migrarea antrenarii in Cloud (Google Colab).
2. **Rezolutie Imagine:** Limitarea la 150x150 pixeli (pentru viteza) face ca defectele foarte mici (zgarieturi fine) sa fie uneori pierdute.
3. **Iluminare:** Modelul este sensibil la variatii mari de iluminare, performand mai slab pe imagini subexpuse.

### 5.3 Lectii Invatate
1. **Cloud vs Local:** Pentru Deep Learning, mediile cloud (Colab/Kaggle) sunt mult mai stabile si rapide decat configurarea locala, mai ales pe hardware non-NVIDIA.
2. **Importanta Datelor:** Curatarea datelor si balansarea claselor au avut un impact mai mare asupra performantei decat simpla modificare a hiperparametrilor.
3. **Iterativitate:** Abordarea incrementala (Schelet -> Baseline -> Optimizat) a permis identificarea rapida a blocajelor (ex: pipeline-ul de date).

---

## Structura Repository-ului la Finalul Etapei 6