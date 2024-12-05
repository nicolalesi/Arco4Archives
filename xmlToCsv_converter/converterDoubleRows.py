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
        "relazione_bib","id_sistema"]

rows = []

# Parsing del file XML
xmlparse = Xet.parse('sab_trentino_secondo_caricamento_EAC.xml')
root = xmlparse.getroot()

# Definisci i namespaces
# Definisci i namespaces
namespaces = {
    'eac-cpf': 'urn:isbn:1-931666-33-4',
    'icar-import': 'http://www.san.beniculturali.it/icar-import'
}

# Esegui il parsing degli elementi e associa ID ai record
id_map = []  # Lista per mappare id_sistema e cpfDescription
for record in root.findall('.//icar-import:record', namespaces):
    record_id = record.find('.//icar-import:recordHeader/icar-import:id', namespaces)
    if record_id is not None:
        id_sistema = record_id.text
        cpf_description = record.find('.//eac-cpf:cpfDescription', namespaces)
        if cpf_description is not None:
            id_map.append((id_sistema, cpf_description))

# Estrai i dati dal file XML
rows = []

for id_sistema, cpf_description in id_map:
    # Estraiamo tutti i valori dai tag
    field_mappings = {
        "legalName": cpf_description.findall('.//eac-cpf:nameEntry/eac-cpf:part', namespaces),
        "altraDenominazione": cpf_description.findall('.//eac-cpf:nameEntry[@localType="altraDenominazione"]/eac-cpf:part', namespaces),
        "dataAltraDenominazione": cpf_description.findall('.//eac-cpf:nameEntry[@localType="altraDenominazione"]/eac-cpf:useDates/eac-cpf:date', namespaces),
        "localType": cpf_description.findall('.//eac-cpf:identity/eac-cpf:entityType', namespaces),
        "nome": cpf_description.findall('.//eac-cpf:identity/eac-cpf:nameEntry/eac-cpf:part[@localType="nome"]', namespaces),
        "cognome": cpf_description.findall('.//eac-cpf:identity/eac-cpf:nameEntry/eac-cpf:part[@localType="cognome"]', namespaces),
        "intestazione": cpf_description.findall('.//eac-cpf:identity/eac-cpf:nameEntry[@localType="intestazione"]/eac-cpf:part', namespaces),
        "authorizedFrom": cpf_description.findall('.//eac-cpf:nameEntry/eac-cpf:authorizedForm', namespaces),
        "existenceRangeFromDate": cpf_description.findall('.//eac-cpf:existDates/eac-cpf:dateRange/eac-cpf:fromDate', namespaces),
        "existenceRangeToDate": cpf_description.findall('.//eac-cpf:existDates/eac-cpf:dateRange/eac-cpf:toDate', namespaces),
        "dataNascita": cpf_description.findall('.//eac-cpf:existDates/eac-cpf:dateSet/eac-cpf:date[@localType="dataNascita"]', namespaces),
        "dataMorte": cpf_description.findall('.//eac-cpf:existDates/eac-cpf:dateSet/eac-cpf:date[@localType="dataMorte"]', namespaces),
        "placeRole": cpf_description.findall('.//eac-cpf:place/eac-cpf:placeRole', namespaces),
        "placeEntry": cpf_description.findall('.//eac-cpf:place/eac-cpf:placeEntry', namespaces),
        "otherPlaceRole": cpf_description.findall('.//eac-cpf:place/eac-cpf:placeRole', namespaces),
        "otherPlaceEntry": cpf_description.findall('.//eac-cpf:place/eac-cpf:placeEntry', namespaces),
        "professione": cpf_description.findall('.//eac-cpf:localDescription[@localType="professione"]/eac-cpf:term', namespaces),
        "legalStatus": cpf_description.findall('.//eac-cpf:description/eac-cpf:legalStatuses/eac-cpf:legalStatus/eac-cpf:term', namespaces),
        "tipologiaEnte": cpf_description.findall('.//eac-cpf:localDescription[@localType="tipologiaEnte"]/eac-cpf:term', namespaces),
        "history" : cpf_description.findall('.//eac-cpf:description/eac-cpf:biogHist/eac-cpf:p', namespaces),
        "genere": cpf_description.findall('.//eac-cpf:localDescription[@localType="genere"]/eac-cpf:term', namespaces),
        "relazione_complesso": cpf_description.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="complesso"]', namespaces),
        "relazione_tema": cpf_description.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="TEMA"]', namespaces),
        "relazione_bib": cpf_description.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="BIBTEXT"]', namespaces)
    }

    # Crea una riga di base con id_sistema
    base_row = {"id_sistema": id_sistema}

    # Aggiungi i valori unici o predefiniti alla riga di base
    for field, values in field_mappings.items():
        base_row[field] = values[0].text if values else None

    rows.append(base_row)

    # Aggiungi una riga per ogni occorrenza multipla
    for field, values in field_mappings.items():
        if len(values) > 1:  # Se ci sono più occorrenze
            for value in values:
                new_row = base_row.copy()  # Crea una nuova copia della riga di base
                new_row[field] = value.text
                rows.append(new_row)

# Creazione del DataFrame
df = pd.DataFrame(rows)

# Scrivi il DataFrame nel CSV
df.to_csv('outputDoubleRows.csv', index=False)

print("File CSV creato con successo.")
