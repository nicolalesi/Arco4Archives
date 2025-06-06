import spacy
from SPARQLWrapper import SPARQLWrapper, JSON

# Carica modello italiano spaCy
nlp = spacy.load("it_core_news_lg")

# SPARQL endpoint ArCo
sparql = SPARQLWrapper("https://dati.beniculturali.it/sparql")
sparql.setReturnFormat(JSON)

# Funzione per costruire query SPARQL dinamica
def costruisci_query(bene_culturale):
    return f"""
    PREFIX l0: <https://w3id.org/italia/onto/l0/>
    PREFIX cis: <http://dati.beniculturali.it/cis/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?eventName
    WHERE {{
      ?event cis:involvesCulturalEntity ?culturalProperty ;
             l0:name ?eventName .
      ?culturalProperty rdfs:label ?label .
      FILTER(CONTAINS(LCASE(?label), LCASE("{bene_culturale}")))
    }}
    LIMIT 5
    """

# Estrai entità rilevanti dalla domanda
def estrai_bene_culturale(domanda):
    doc = nlp(domanda)
    for ent in doc.ents:
        if ent.label_ in ["LOC", "ORG", "PER", "MISC"]:  # bene culturale spesso è un luogo/organizzazione
            return ent.text
    # fallback: prendi ultima parola importante
    tokens = [t.text for t in doc if not t.is_stop and t.is_alpha]
    return " ".join(tokens[-2:]) if tokens else None

# Rispondi alla domanda
def rispondi(domanda):
    bene = estrai_bene_culturale(domanda)
    if not bene:
        print("Non ho capito a quale bene culturale ti riferisci.")
        return

    print(f"\n🎯 Cerco eventi legati a: {bene}")
    sparql.setQuery(costruisci_query(bene))
    results = sparql.query().convert()

    eventi = [r["eventName"]["value"] for r in results["results"]["bindings"]]
    if eventi:
        print("\n📍 Eventi trovati:")
        for ev in eventi:
            print(f"– {ev}")
    else:
        print("\n😕 Nessun evento trovato per questo bene.")

# Avvio chatbot
while True:
    domanda = input("\nFai una domanda (es: Quali eventi riguardano il Colosseo?)\n> ")
    if domanda.lower() in ["esci", "exit", "quit"]:
        break
    rispondi(domanda)
