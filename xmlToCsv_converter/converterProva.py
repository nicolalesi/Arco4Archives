import xml.etree.ElementTree as Xet
import pandas as pd

def exist(v):
    return len(v) > 0

def occorrenze(v):
    return len(v) > 1

# Colonne definite per il CSV
cols = ["legalName", "altraDenominazione", "dataAltraDenominazione", "localType", "nome", "cognome", 
        "intestazione", "authorizedFrom", "existenceRangeFromDate", "existenceRangeToDate", "dataNascita", 
        "dataMorte", "placeRole", "placeEntry", "otherPlaceRole", "otherPlaceEntry", "professione", 
        "legalStatus", "tipologiaEnte", "history", "genere", "relazione_complesso", "relazione_tema", 
        "relazione_bib"]

rows = []

# Parsing del file XML
xmlparse = Xet.parse('sab_trentino_secondo_caricamento_EAC.xml')
root = xmlparse.getroot()

# Definisci i namespaces
namespaces = {
    'eac-cpf': 'urn:isbn:1-931666-33-4',
    'icar-import': 'http://www.san.beniculturali.it/icar-import'
}

# Estrai i dati dal file XML
for i in root.findall('.//eac-cpf:cpfDescription', namespaces):
    # Estraiamo tutti i valori dai tag
    field_mappings = {
        "legalName": i.findall('.//eac-cpf:nameEntry/eac-cpf:part', namespaces),
        "altraDenominazione": i.findall('.//eac-cpf:nameEntry[@localType="altraDenominazione"]/eac-cpf:part', namespaces),
        "dataAltraDenominazione": i.findall('.//eac-cpf:nameEntry[@localType="altraDenominazione"]/eac-cpf:useDates/eac-cpf:date', namespaces),
        "localType": i.findall('.//eac-cpf:identity/eac-cpf:entityType', namespaces),
        "nome": i.findall('.//eac-cpf:identity/eac-cpf:nameEntry/eac-cpf:part[@localType="nome"]', namespaces),
        "cognome": i.findall('.//eac-cpf:identity/eac-cpf:nameEntry/eac-cpf:part[@localType="cognome"]', namespaces),
        "intestazione": i.findall('.//eac-cpf:identity/eac-cpf:nameEntry[@localType="intestazione"]/eac-cpf:part', namespaces),
        "authorizedFrom": i.findall('.//eac-cpf:nameEntry/eac-cpf:authorizedForm', namespaces),
        "existenceRangeFromDate": i.findall('.//eac-cpf:existDates/eac-cpf:dateRange/eac-cpf:fromDate', namespaces),
        "existenceRangeToDate": i.findall('.//eac-cpf:existDates/eac-cpf:dateRange/eac-cpf:toDate', namespaces),
        "dataNascita": i.findall('.//eac-cpf:existDates/eac-cpf:dateSet/eac-cpf:date[@localType="dataNascita"]', namespaces),
        "dataMorte": i.findall('.//eac-cpf:existDates/eac-cpf:dateSet/eac-cpf:date[@localType="dataMorte"]', namespaces),
        "placeRole": i.findall('.//eac-cpf:place/eac-cpf:placeRole', namespaces),
        "placeEntry": i.findall('.//eac-cpf:place/eac-cpf:placeEntry', namespaces),
        "otherPlaceRole": i.findall('.//eac-cpf:place/eac-cpf:placeRole', namespaces),
        "otherPlaceEntry": i.findall('.//eac-cpf:place/eac-cpf:placeEntry', namespaces),
        "professione": i.findall('.//eac-cpf:localDescription[@localType="professione"]/eac-cpf:term', namespaces),
        "legalStatus": i.findall('.//eac-cpf:description/eac-cpf:legalStatuses/eac-cpf:legalStatus/eac-cpf:term', namespaces),
        "tipologiaEnte": i.findall('.//eac-cpf:localDescription[@localType="tipologiaEnte"]/eac-cpf:term', namespaces),
        "genere": i.findall('.//eac-cpf:localDescription[@localType="genere"]/eac-cpf:term', namespaces),
        "relazione_complesso": i.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="complesso"]', namespaces),
        "relazione_tema": i.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="TEMA"]', namespaces),
        "relazione_bib": i.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="BIBTEXT"]', namespaces)
    }

    # Crea una riga di base
    base_row = {}

    # Aggiungi i valori unici (prima occorrenza) alla riga di base
    for field, values in field_mappings.items():
        if exist(values):
            base_row[field] = values[0].text

    # Aggiungi la riga di base alla lista delle righe
    rows.append(base_row.copy())

    # Aggiungi una riga per ogni occorrenza multipla
    for field, values in field_mappings.items():
        if occorrenze(values):
            for value in values:
                new_row = base_row.copy()  # Crea una nuova copia della riga di base
                new_row[field] = value.text
                rows.append(new_row)

# Creazione del DataFrame
df = pd.DataFrame(rows, columns=cols)

# Scrivi il DataFrame nel CSV
df.to_csv('output.csv', index=False)

print("File CSV creato con successo.")
