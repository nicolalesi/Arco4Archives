import xml.etree.ElementTree as Xet
import pandas as pd

def check_n_entries(nameColumn,vectorOfColumns):
    if len(nameColumn)>1:
        vectorOfColumns.append(nameColumn)
        return vectorOfColumns
    return False
        

# Colonne definite per il CSV
cols = ["legalName","altraDenominazione","dataAltraDenominazione","localType","nome","cognome","intestazione","authorizedFrom", "existenceRangeFromDate", "existenceRangeToDate","dataNascita","dataMorte", "placeRole", "placeEntry","otherPlaceRole","otherPlaceEntry","professione","legalStatus", "tipologiaEnte", "history","genere", "relazione_complesso"]
rows = []

# Parsing del file XML
xmlparse = Xet.parse('sab_trentino_secondo_caricamento_EAC.xml')
root = xmlparse.getroot()

# Definisci i namespaces
namespaces = {
    'eac-cpf': 'urn:isbn:1-931666-33-4',
    'icar-import':'http://www.san.beniculturali.it/icar-import'
}

# Estrai i dati dal file XML
for i in root.findall('.//eac-cpf:cpfDescription', namespaces):

    legalName = i.find('.//eac-cpf:nameEntry/eac-cpf:part', namespaces)
    legalName_text = legalName.text if legalName is not None else None

    altraDenominazione=i.find('.//eac-cpf:nameEntry[@localType="altraDenominazione"]/eac-cpf:part', namespaces)
    altraDenominazione_text = altraDenominazione.text if altraDenominazione is not None else None

    dateAltraDenominazione=i.find('.//eac-cpf:nameEntry[@localType="altraDenominazione"]/eac-cpf:useDates/eac-cpf:date', namespaces)
    dateAltraDenominazione_text = dateAltraDenominazione.text if dateAltraDenominazione is not None else None

    localType = i.find('.//eac-cpf:identity/eac-cpf:entityType', namespaces)
    localType_text = localType.text if localType is not None else None

    nome = i.find('.//eac-cpf:identity/eac-cpf:nameEntry/eac-cpf:part[@localType="nome"]', namespaces)
    nome_text = nome.text if nome is not None else None

    cognome = i.find('.//eac-cpf:identity/eac-cpf:nameEntry/eac-cpf:part[@localType="cognome"]', namespaces)
    cognome_text = cognome.text if cognome is not None else None

    intestazione = i.find('.//eac-cpf:identity/eac-cpf:nameEntry[@localType="intestazione"]/eac-cpf:part', namespaces)
    intestazione_text = intestazione.text if intestazione is not None else None

    authorizedFrom = i.find('.//eac-cpf:nameEntry/eac-cpf:authorizedForm', namespaces)
    authorizedFrom_text = authorizedFrom.text if authorizedFrom is not None else None

    existenceRangeFromDate = i.find('.//eac-cpf:existDates/eac-cpf:dateRange/eac-cpf:fromDate', namespaces)
    existenceRangeFromDate_text = existenceRangeFromDate.text if existenceRangeFromDate is not None else None

    existenceRangeToDate = i.find('.//eac-cpf:existDates/eac-cpf:dateRange/eac-cpf:toDate', namespaces)
    existenceRangeToDate_text = existenceRangeToDate.text if existenceRangeToDate is not None else None

    dataNascita = i.find('.//eac-cpf:existDates/eac-cpf:dateSet/eac-cpf:date[@localType="dataNascita"]', namespaces)
    dataNascita_text = dataNascita.text if dataNascita is not None else None

    dataMorte = i.find('.//eac-cpf:existDates/eac-cpf:dateSet/eac-cpf:date[@localType="dataMorte"]', namespaces)
    dataMorte_text = dataMorte.text if dataMorte is not None else None

    placeRole = i.find('.//eac-cpf:place/eac-cpf:placeRole', namespaces)
    placeRole_text = placeRole.text if placeRole is not None else None

    placeEntry = i.find('.//eac-cpf:place/eac-cpf:placeEntry', namespaces)
    placeEntry_text = placeEntry.text if placeEntry is not None else None

    otherPlaceRole = i.findall('.//eac-cpf:place/eac-cpf:placeRole', namespaces)
    otherPlaceRole_text=""
    if len(otherPlaceRole)>1:
        otherPlaceRole=otherPlaceRole[1]
        otherPlaceRole_text = otherPlaceRole.text if otherPlaceRole is not None else None

    otherPlaceEntry = i.findall('.//eac-cpf:place/eac-cpf:placeEntry', namespaces)
    otherPlaceEntry_text=""
    if len(otherPlaceEntry)>1:
        otherPlaceEntry=otherPlaceEntry[1]
        otherPlaceEntry_text = otherPlaceEntry.text if otherPlaceEntry is not None else None

    professione = i.find('.//eac-cpf:localDescription[@localType="professione"]/eac-cpf:term', namespaces)
    professione_text = professione.text if professione is not None else None

    legalStatus = i.find('.//eac-cpf:description/eac-cpf:legalStatuses/eac-cpf:legalStatus/eac-cpf:term', namespaces)
    legalStatus_text = legalStatus.text if legalStatus is not None else None

    #Con lo stesso percorso c'è anche genere 
    tipologiaEnte = i.find('.//eac-cpf:localDescription[@localType="tipologiaEnte"]/eac-cpf:term', namespaces)
    tipologia_text = tipologiaEnte.text if tipologiaEnte is not None else None

    #Bisogna verificare se prende solo il primo, per ora commentiamo
    #history = i.find('.//eac-cpf:description/eac-cpf:biogHist/eac-cpf:p', namespaces)
    #history_text = history.text if history is not None else None

    genere = i.find('.//eac-cpf:localDescription[@localType="genere"]/eac-cpf:term', namespaces)
    genere_text = genere.text if genere is not None else None

    #Viene presa solo la prima relazione, bisognerebbe creare dinamicamente delle nuove colonne o prevederle dal principio
    relationCA = i.find('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry[@localType="complesso"]', namespaces)
    relationCA_text = relationCA.text if relationCA is not None else None

    #Aggiunge righe se ci sono relazioni non previste manualmente
    otherRelations=i.findall('.//eac-cpf:relations/eac-cpf:resourceRelation/eac-cpf:relationEntry', namespaces)
    otherRelations_text=""
    relations={}
    if len(otherRelations)>1:
        for i in otherRelations:
            otherRelations_text=i.text
            #print(otherRelations_text)
            localTypeValue=i.attrib['localType']
            toCompare="relazione_"+localTypeValue
            chiave="relazione_"+localTypeValue
            if (toCompare in cols)==False:
                cols.append("relazione_"+localTypeValue)
                chiave="relazione_"+localTypeValue
                relations= {chiave:otherRelations_text}
            else :
                    relations[chiave]=otherRelations_text

                
    #Forse è meglio caricare i valori row uno alla volta
    # Aggiungi i dati estratti alla lista rows
    row ={"legalName": legalName_text,
                 "localType":localType_text,
                 "altraDenominazione":altraDenominazione_text,
                 "dataAltraDenominazione":dateAltraDenominazione_text,
                 "nome":nome_text,
                 "cognome":cognome_text,
                 "intestazione":intestazione_text,
                 "authorizedFrom":authorizedFrom_text,
                 "existenceRangeFromDate":existenceRangeFromDate_text,
                 "existenceRangeToDate":existenceRangeToDate_text,
                 "dataNascita":dataNascita_text,
                 "dataMorte":dataMorte_text,
                 "placeRole":placeRole_text,
                 "placeEntry":placeEntry_text,
                 "otherPlaceRole": otherPlaceRole_text,
                 "otherPlaceEntry":otherPlaceEntry_text,
                 "professione": professione_text,
                 "legalStatus":legalStatus_text,
                 "tipologiaEnte":tipologia_text,
                 "genere":genere_text,
                 "relazione_complesso":relationCA_text,
                 }
    
    row.update(relations)

    rows.append(row)

    vectorOfValues={"legalName":legalName,
                    "localType":localType,
                    "altraDenominazione":altraDenominazione,
                    "dataAltraDenominazione":dateAltraDenominazione,
                    "nome":nome,
                    "cognome":cognome,
                    "intestazione":intestazione,
                    "authorizedFrom":authorizedFrom,
                    "existenceRangeFromDate":existenceRangeFromDate,
                    "existenceRangeToDate":existenceRangeToDate,
                    "dataNascita":dataNascita,
                    "dataMorte":dataMorte,
                    "placeRole":placeRole,
                    "placeEntry":placeEntry,
                    "otherPlaceRole":otherPlaceRole,
                    "otherPlaceEntry":otherPlaceEntry,
                    "professione":professione,
                    "legalStatus":legalStatus,
                    "tipologiaEnte":tipologiaEnte,
                    "genere":genere,
                    "relazione_complesso":relationCA
                    }




    


# Creazione del DataFrame
df = pd.DataFrame(rows, columns=cols)

# Scrivi il DataFrame nel CSV
df.to_csv('output.csv', index=False)

print("File CSV creato con successo.")
