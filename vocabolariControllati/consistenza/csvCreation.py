import pandas as pd

# Creazione del DataFrame con i dati forniti
data = {
    "label_IT": [
        "Busta", "Carta", "Cartella", "Faldone", "Fascicolo", "Filza", "Foglio", "Manifesto",
        "Mappa", "Mazzo", "Opuscolo", "Pacco", "Pagina", "Plico", "Quaderno", "Raccoglitore",
        "Registro", "Rivista", "Rotolo", "Scatola", "Scheda", "Taccuino", "Vacchetta", "Volume", "Album"
    ],
    "label_EN": [
        "Envelope", "Folio", "Folder", "File", "Dossier", "Bundle", "Leaf", "Poster", 
        "Map", "Set", "Brochure", "Archives box", "Page", "Container", "Journal", "Collector",
        "Register", "Magazine", "Roll", "Case file", "Card Catalog", "Field Book", "Ledger", "Volume", "Album"
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
        "Envelope", "Folio", "Folder", "File", "Dossier", "Bundle", "Leaf", "Poster",
        "Map", "Set", "Brochure", "Archives Box", "Page", "Container", "Journal", "Collector",
        "Register", "Magazine", "Roll", "Case file", "Card Catalog", "Field Book", "Ledger", "Volume", "Album"
    ],
    "altLabel_IT": ["" for _ in range(25)],
    "altLabel_EN": ["" for _ in range(25)],
    #Le definizioni sono diverse, e non una la traduzione dell'altra, per fare in modo di poterle comparare e appurare la correttezza della traduzione
    "definition_IT": [
        "Una busta è tipicamente costituita da carta, piegata e incollata in modo che un lato rimanga aperto per consentire l'inserimento di un documento piatto, eventualmente dopo essere stato piegato, e con un lembo che consente la chiusura della busta. Le buste di formato standard includono la lettera", 
        "Foglio di carta o di cartoncino, contenente documenti archivistici.", 
        "Unità di consistenza. È il contenitore nel quale vengono raccolti e conservati i fascicoli o - nel caso di atti singoli non raggruppati in fascicoli - i documenti sciolti.", 
        "Cartella robusta, spesso chiusa con due nastrini e fettucce annodate, che racchiude e protegge una serie di incartamenti.", 
        "Strumento di raccolta degli atti e dei documenti inerenti al processo.", 
        "Unità di consistenza. È il contenitore nel quale vengono raccolti e conservati i fascicoli o - nel caso di atti singoli non raggruppati in fascicoli - i documenti sciolti. Si usano come sinonimo di busta le parole faldone e cartella. Si possono trovare usate nello stesso senso anche le parole mazzo, fascio, pacco, filza", 
        "Foglio di carta o di cartoncino, contenente documenti archivistici.", 
        "Foglio di carta, più o meno ampio, che si affigge sui muri delle strade, o su sostegni fissi appositamente collocati, per rendere noto a tutti ciò che vi è stampato.",
        "Ogni rappresentazione grafica piana di una porzione della superficie terrestre (lo stesso che carta geografica o topografica) e, estensiv., della superficie di un corpo in genere.", 
        "Unità di consistenza. È il contenitore nel quale vengono raccolti e conservati i fascicoli o - nel caso di atti singoli non raggruppati in fascicoli - i documenti sciolti. Si usano come sinonimo di busta le parole faldone e cartella. Si possono trovare usate nello stesso senso anche le parole mazzo, fascio, pacco, filza", 
        "Breve opera, libretto di poche pagine: un o. di critica storica; gli o. morali di Plutarco; oggi si dice spec. di pubblicazioni a carattere propagandistico o divulgativo: un o. informativo, turistico, pubblicitario.",
        "Unità di consistenza. È il contenitore nel quale vengono raccolti e conservati i fascicoli o - nel caso di atti singoli non raggruppati in fascicoli - i documenti sciolti. Si usano come sinonimo di busta le parole faldone e cartella. Si possono trovare usate nello stesso senso anche le parole mazzo, fascio, pacco, filza", 
        "Si chiama PAGINA ciascuna delle due facce di un foglio di carta, isolato o unito ad altri in un quaderno, un libro o un giornale.", 
        "Insieme di carte di varia natura (lettere, documenti e sim.), disposte, piegate o no, in una busta o in un pacco", 
        "Insieme di fogli di carta da scrivere, raccolti e legati in una copertina di cartoncino, destinato a usi scolastici, per conti, appunti e annotazioni.", 
        "Oggetto, dispositivo, impianto che serve a raccogliere.",
        "Unità archivistica costituita da un insieme di fogli rilegati. Nel registro vengono trascritti o registrati per esteso o per sunto documenti e minute di documenti, ovvero vengono effettuate trascrizioni, registrazioni e annotazioni costitutive dell'atto giuridico.", 
        "Pubblicazione periodica che ha generalm. per oggetto un particolare settore di studî o di attività, con interessi prevalentemente critici e di aggiornamento", 
        "Unità archivistica formata da un foglio cartaceo o pergamenaceo, o da più fogli cuciti l’uno all’altro, conservati arrotolati. Si trovano frequentemente conservati in rotolo pergamene e mappe.",
        "Contenitore di cartone, o di tela e cartone nel quale i documenti sono conservati disposti in senso orizzontale.", 
        "S. analitica, quella che contiene particolari indicazioni sul contenuto del libro, o anche descrizioni molto estese e minuziose.", 
        "Libriccino con fogli bianchi per appunti: segnare una data, un appuntamento sul t.; un t. rilegato in pelle.",
        "Nome usato anticam., e oggi conservato in alcune regioni, per indicare libretti o registri, per lo più di forma oblunga, e in origine coperti con pelle di vacchetta.",
        "Unità archivistica costituita di più fogli rilegati insieme. La parola attiene all'aspetto esterno dei documenti e distingue quelli che si presentano come unità rilegate rispetto a quelli sciolti conservati in buste. Di fatto la parola viene usata spesso come sinonimo di registro.",
        "Quaderno o libro rilegato per raccogliere versi, firme, ritratti, cartoline, ricordi, o per altri usi particolari"
    ],
     "definition_EN": [
        "An envelope1 is typically made of paper, folded and glued so that one side remains open to allow a flat document to be inserted, possibly after being folded, and with a flap that allows the envelope to be sealed.", 
        "A single leaf in a book or a manuscript.", " sheet of heavy paper stock or cardboard, scored near the middle, its halves bent so they rest side by side, and used as a loose cover to keep documents and other flat materials together, especially for purposes of filing.", 
        "A group of documents related by use or topic, typically housed in a folder (or a group of folders for a large file)",
        "A group of documents assembled to provide information about a specific topic.", 
        "A group of individual documents, normally tied together by string, linen tape, or the like.", 
        "A sheet of paper or parchment.", 
        "A printed illustration on a large sheet. A large, flexible sheet bearing text, usually illustrated, that is publicly displayed to advertise or promote something.", 
        "A graphic representation of features of the Earth or another celestial body.", 
        "A set of archival or (more commonly) manuscript materials.", 
        "A short printed work, sometimes a leaflet, providing general information about an organization or service.",
        "A container made from materials appropriate for the long-term storage of archival materials.",
        "A sheet of paper, especially one bound in a publication; a leaf.", "A package or housing used to hold materials; a receptacle.", 
        "An impartial record of an organization's events, proceedings, and actions.", 
        "An individual, or group of individuals, responsible for acquiring materials.",
        "A book or record listing information in a consistent format", 
        "A publication, often illustrated, containing essays, articles, short stories, poems, or other short works, issued periodically and directed to a popular audience.",
        "A document wound into a cylinder; a scroll.", 
        "A collection of documents relating to a particular investigation or in support of some administrative action", 
        "Descriptions of materials, with each entry on a separate card (or cards), systematically arranged to facilitate access.", 
        "Volumes containing notes made while working at a site (in the field) to make a record of observations and discoveries.", 
        "A document containing a record of debits, credits, and other financial transactions, typically organized into separate accounts.", 
        "A collection of pages bound together.", 
        "A volume of blank pages, bound or loose leaf, used to collect photographs, documents, clippings, and the like."
    ],
    "notation": [
        "envelope", "folio", "folder", "file", "dossier", "bundle", "leaf", "poster", 
        "map", "set", "brochure", "archivesbox", "page", "container", "journal", "collector",
        "register", "magazine", "roll", "casefile", "cardcatalog", "fieldbook", "ledger", "volume", "album"
    ],
    "note": ["" for _ in range(25)],
}

# Creazione del DataFrame
df = pd.DataFrame(data)

# Salvataggio del DataFrame come file CSV
file_path = "archives-consistency-type.csv"
df.to_csv(file_path, index=False)

print(f"File salvato correttamente in: {file_path}")
