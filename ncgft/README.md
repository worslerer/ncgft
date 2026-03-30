# ncgft

Repozytorium jest zorganizowane wokol trzech podprojektow:

- `fine_tune/` - trening i dostrajanie modeli
- `generation/` - generowanie raportow lub tekstu
- `ner_class/` - NER i klasyfikacja
- `shared/` - wspolne narzedzia, klasy i konfiguracja
- `notebooks/` - eksperymenty laczace elementy z roznych modulow

Kazdy podprojekt trzyma kod w `src/`, konfiguracje w `cfg/` i lokalne dane w `data/`.
Notebooki sa wspolne celowo, zeby latwo laczyc komponenty z wielu modulow w jednym eksperymencie.

Zalecenie organizacyjne:

- logika biznesowa, funkcje i klasy trafiaja do `src/`
- parametry i stale do `cfg/`
- notebooki tylko uruchamiaja eksperymenty i analizy
- elementy wspolne dla wielu podprojektow trafiaja do `shared/`

