import pandas as pd

# Creazione del DataFrame con i dati forniti
data = {
    "label_IT": [
        "Busta", "Carta", "Cartella", "Faldone", "Fascicolo", "Filza", "Foglio", "Manifesto",
        "Mappa", "Mazzo", "Opuscolo", "Pacco", "Pagina", "Plico", "Quaderno", "Raccoglitore",
        "Registro", "Rivista", "Rotolo", "Scatola", "Scheda", "Taccuino", "Vacchetta", "Volume", "Album"
    ],
    "label_EN": [
        "envelope", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", ""
    ],
    "prefLabel": [
        "Busta", "Carta", "Cartella", "Faldone", "Fascicolo", "Filza", "Foglio", "Manifesto",
        "Mappa", "Mazzo", "Opuscolo", "Pacco", "Pagina", "Plico", "Quaderno", "Raccoglitore",
        "Registro", "Rivista", "Rotolo", "Scatola", "Scheda", "Taccuino", "Vacchetta", "Volume", "Album"
    ],
    "prefLabel_IT": [
        "Busta", "Carta", "Cartella", "Faldone", "Fascicolo", "Filza", "Foglio", "Manifesto",
        "Mappa", "Mazzo", "Opuscolo", "Pacco", "Pagina", "Plico", "Quaderno", "Raccoglitore",
        "Registro", "Rivista", "Rotolo", "Scatola", "Scheda", "Taccuino", "Vacchetta", "Volume", "Album"
    ],
    "prefLabel_EN": [
        "envelope", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", ""
    ],
    "altLabel_IT": ["" for _ in range(25)],
    "altLabel_EN": ["" for _ in range(25)],
    "definition_IT": ["" for _ in range(25)],
    "definition_EN": ["" for _ in range(25)],
    "notation": ["" for _ in range(25)],
    "note": ["" for _ in range(25)],
}

# Creazione del DataFrame
df = pd.DataFrame(data)

# Salvataggio del DataFrame come file CSV
file_path = "archives-consistency-type.csv"
df.to_csv(file_path, index=False)

print(f"File salvato correttamente in: {file_path}")
