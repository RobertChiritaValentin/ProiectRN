# Documentatie Set de Date - VisInspAI

## 1. Descriere Generala
Setul de date este compus din imagini reprezentand suprafete metalice, clasificate in 6 categorii distincte de defecte industriale:
* **Crazing**: Fisuri
* **Inclusion**: Particule straine incluse in material
* **Patches**: Pete sau neregularitati de textura
* **Pitted Surface**: Cavitati mici cauzate de coroziune
* **Rolled-in Scale**: Oxid de fier presat in suprafata
* **Scratches**: Zgarieturi liniare mecanice

## 2. Preprocesare Date
Toate imaginile brute (Raw) au fost supuse unui pipeline de procesare automata prin scriptul `@resize.py`:
* **Redimensionare**: 150x150 pixeli pentru uniformitatea input-ului in reteaua CNN.
* **Conversie Culoare**: Greyscale pentru reducerea complexitatii si concentrarea pe texturi.
* **Normalizare**: Valorile pixelilor sunt scalate in intervalul [0, 1] prin rescale 1./255 in timpul antrenarii.

## 3. Statistici si Performanta
* **Distributie**: Datele sunt impartite in seturi de Train (70%) si Validation (15%), Test (15%).
* **Acuratete**: Modelul optimizat atinge o precizie de validare de aproximativ 96%.
* **Analiza Erorilor**: Consultati `confusion_matrix_optimized.png` pentru a vedea performanta modelului pe fiecare clasa in parte.

## 4. Fisiere Incluse
* `loss_curve.png`: Evolutia functiei de pierdere pe parcursul celor 15 epoci.
* `confusion_matrix.png`: Matricea de confuzie rezultata in urma evaluarii pe setul de test.
