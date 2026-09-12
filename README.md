# Auftrag

1. Implementiert in `main.py` einen Taschenrechner mit den vier Grundrechenarten. Für jede
   Rechenart soll eine eigene Funktion erstellt werden.
2. Die Division durch 0 ist nicht erlaubt.
3. Testet den Taschenrechner händisch. Testet auch die Division durch 0.
4. Erstellt nun ein neues File `test_main.py` und erstellt einen Test für jeden Rechentypen.
   Jede Testfunktion muss mit `test_` beginnen, sonst findet pytest sie nicht.

   Hinweis: für die Tests müssen folgende imports hinzugefügt werden

```python
   from main import addieren
```

   Die übrigen Funktionen müssen ebenfalls importiert werden.

5. Schreibt zusätzlich einen Test für die Division durch 0.
6. Führt die Tests mit `pytest` aus. Alle Tests müssen durchlaufen.
7. Erstellt einen neuen Branch, commitet und pusht eure Lösung.
8. Vergleicht eure Lösung mit einer anderen Person aus der Klasse.