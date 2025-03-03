import pandas as pd

# Creazione del DataFrame con i dati forniti
data = {
    "label_IT": [
        "Acquaforte", "Acquerello", "Acquatina", "Algrafia", "Altro", "Blu print", "Bulino", 
        "Calcografia", "Camaïeu", "Carborundum", "Chiaroscuro", "Cliché-verre", "Collage", 
        "Collografia", "Coloritura", "Computergrafica", "Cromolitografia", "Cromozincografia", 
        "Doratura", "Eliografia", "Eliotipia", "Fotoincisione", "Fotolitografia", "Gipsografia", 
        "Lavis", "Linoleografia", "Litografia", "Offset", "Oleografia", "Pochoir", "Puntasecca", 
        "Serigrafia", "Stampa tipografica", "Vernice molle", "Vitrografia", "Xilografia",
        "Albumina", "Ambrotipo", "Aristotipo", "Autocromia", "Calotipo", "Carbone", "Carta salata", 
        "Collodio", "Collotipia", "Dagherrotipo", "Fotografia digitale (chiave USB)", 
        "Fotografia digitale (disco magnetico-ottico)", "Fotoincisione", "Gelatina ai sali d’argento", 
        "Gelatina bromuro d’argento", "Gelatina cloruro d’argento", "Gomma bicromatata", "Platinotipia", 
        "Stampa ai pigmenti", "Stampa a sublimazione", "Stampa fotomeccanica a retino", 
        "Stampa inkjet inchiostri a…", "Tecniche varie", "Cianografia", "Disegno", "Ignoto", "Incisione", 
        "Manoscritto"
    ],
     "label_EN": [
        "Etching", "Watercolor", "Aquarelle", "Autography", "Other", "Blue print", "Engraving", 
        "Calcography", "Chiaroscuro", "Carborundum", "Chiaroscuro", "Cliché-verre", "Collage", 
        "Collography", "Coloring", "Computer graphics", "Chromolithography", "Chromozincography", 
        "Gilding", "Eliography", "Eliotypy", "Photogravure", "Photolithography", "Gypsography", 
        "Lavis", "Linocut", "Lithography", "Offset", "Oil painting", "Pochoir", "Drypoint", 
        "Silkscreen", "Letterpress printing", "Soft varnish", "Vitrography", "Woodcut",
        "Albumen", "Ambrotype", "Aristotype", "Autochrome", "Calotype", "Carbon print", "Salted paper", 
        "Collodion", "Collotype", "Daguerreotype", "Digital photography (USB key)", 
        "Digital photography (magnetic-optical disk)", "Photogravure", "Silver salts gelatin", 
        "Silver bromide gelatin", "Silver chloride gelatin", "Bichromate gum", "Platinotype", 
        "Pigment printing", "Sublimation printing", "Photomechanical screen printing", 
        "Inkjet printing inks", "Various techniques", "Cyanotype", "Drawing", "Unknown", "Engraving", 
        "Manuscript"
    ],
    "prefLabel": [
        "Acquaforte", "Acquerello", "Acquatina", "Algrafia", "Altro", "Blu print", "Bulino", 
        "Calcografia", "Camaïeu", "Carborundum", "Chiaroscuro", "Cliché-verre", "Collage", 
        "Collografia", "Coloritura", "Computergrafica", "Cromolitografia", "Cromozincografia", 
        "Doratura", "Eliografia", "Eliotipia", "Fotoincisione", "Fotolitografia", "Gipsografia", 
        "Lavis", "Linoleografia", "Litografia", "Offset", "Oleografia", "Pochoir", "Puntasecca", 
        "Serigrafia", "Stampa tipografica", "Vernice molle", "Vitrografia", "Xilografia",
        "Albumina", "Ambrotipo", "Aristotipo", "Autocromia", "Calotipo", "Carbone", "Carta salata", 
        "Collodio", "Collotipia", "Dagherrotipo", "Fotografia digitale (chiave USB)", 
        "Fotografia digitale (disco magnetico-ottico)", "Fotoincisione", "Gelatina ai sali d’argento", 
        "Gelatina bromuro d’argento", "Gelatina cloruro d’argento", "Gomma bicromatata", "Platinotipia", 
        "Stampa ai pigmenti", "Stampa a sublimazione", "Stampa fotomeccanica a retino", 
        "Stampa inkjet inchiostri a…", "Tecniche varie", "Cianografia", "Disegno", "Ignoto", "Incisione", 
        "Manoscritto"
    ],
    "prefLabel_IT": [
        "Acquaforte", "Acquerello", "Acquatina", "Algrafia", "Altro", "Blu print", "Bulino", 
        "Calcografia", "Camaïeu", "Carborundum", "Chiaroscuro", "Cliché-verre", "Collage", 
        "Collografia", "Coloritura", "Computergrafica", "Cromolitografia", "Cromozincografia", 
        "Doratura", "Eliografia", "Eliotipia", "Fotoincisione", "Fotolitografia", "Gipsografia", 
        "Lavis", "Linoleografia", "Litografia", "Offset", "Oleografia", "Pochoir", "Puntasecca", 
        "Serigrafia", "Stampa tipografica", "Vernice molle", "Vitrografia", "Xilografia",
        "Albumina", "Ambrotipo", "Aristotipo", "Autocromia", "Calotipo", "Carbone", "Carta salata", 
        "Collodio", "Collotipia", "Dagherrotipo", "Fotografia digitale (chiave USB)", 
        "Fotografia digitale (disco magnetico-ottico)", "Fotoincisione", "Gelatina ai sali d’argento", 
        "Gelatina bromuro d’argento", "Gelatina cloruro d’argento", "Gomma bicromatata", "Platinotipia", 
        "Stampa ai pigmenti", "Stampa a sublimazione", "Stampa fotomeccanica a retino", 
        "Stampa inkjet inchiostri a…", "Tecniche varie", "Cianografia", "Disegno", "Ignoto", "Incisione", 
        "Manoscritto"
    ],
    "prefLabel_EN": [
        "Etching", "Watercolor", "Aquarelle", "Autography", "Other", "Blue print", "Engraving", 
        "Calcography", "Chiaroscuro", "Carborundum", "Chiaroscuro", "Cliché-verre", "Collage", 
        "Collography", "Coloring", "Computer graphics", "Chromolithography", "Chromozincography", 
        "Gilding", "Eliography", "Eliotypy", "Photogravure", "Photolithography", "Gypsography", 
        "Lavis", "Linocut", "Lithography", "Offset", "Oil painting", "Pochoir", "Drypoint", 
        "Silkscreen", "Letterpress printing", "Soft varnish", "Vitrography", "Woodcut",
        "Albumen", "Ambrotype", "Aristotype", "Autochrome", "Calotype", "Carbon print", "Salted paper", 
        "Collodion", "Collotype", "Daguerreotype", "Digital photography (USB key)", 
        "Digital photography (magnetic-optical disk)", "Photogravure", "Silver salts gelatin", 
        "Silver bromide gelatin", "Silver chloride gelatin", "Bichromate gum", "Platinotype", 
        "Pigment printing", "Sublimation printing", "Photomechanical screen printing", 
        "Inkjet printing inks", "Various techniques", "Cyanotype", "Drawing", "Unknown", "Engraving", 
        "Manuscript"
    ],
    "altLabel_IT": ["" for _ in range(64)],
    "altLabel_EN": ["" for _ in range(64)],
    #Le definizioni sono diverse, e non una la traduzione dell'altra, per fare in modo di poterle comparare e appurare la correttezza della traduzione
    "definition_IT": ["" for _ in range(64)],
    "definition_EN": ["" for _ in range(64)],
    "notation": [
        "acquaforte", "acquerello", "acquatina", "algrafia", "altro", "bluprint", "bulino", 
        "calcografia", "camaieu", "carborundum", "chiaroscuro", "clicheverre", "collage", 
        "collografia", "coloritura", "computergrafica", "cromolitografia", "cromozincografia", 
        "doratura", "eliografia", "eliotipia", "fotoincisione", "fotolitografia", "gipsografia", 
        "lavis", "linoleografia", "litografia", "offset", "oleografia", "pochoir", "puntasecca", 
        "serigrafia", "stampatipografica", "vernicemolle", "vitrografia", "xilografia", 
        "albumina", "ambrotipo", "aristotipo", "autocromia", "calotipo", "carbone", "cartasalata", 
        "collodio", "collotipia", "dagherrotipo", "fotografiadigitalechiaveusb", 
        "fotografiadigitaleddiscomagneticoottico", "fotoincisione", "gelatinaisalidargento", 
        "gelatinabromurodargento", "gelatinaclorurodargento", "gommabicromatata", "platinotipia", 
        "stampaaipigmenti", "stampaasublimazione", "stampafotomeccanicaaretino", 
        "stampainkjetinchiostria", "tecnichevarie", "cianografia", "disegno", "ignoto", "incisione", 
        "manoscritto"
    ],
    "note_EN": ["" for _ in range(64)],
}

# Creazione del DataFrame
df = pd.DataFrame(data)

# Salvataggio del DataFrame come file CSV
file_path = "archives-techniques-type.csv"
df.to_csv(file_path, index=False)

print(f"File salvato correttamente in: {file_path}")
