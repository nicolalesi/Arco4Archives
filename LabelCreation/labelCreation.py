import re
from rdflib import Graph
from lxml import etree as ET
from transformers import MarianMTModel, MarianTokenizer

# Traduttore
tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-it")
model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-it")

def traduci_termine(termine_en):
    inputs = tokenizer(termine_en, return_tensors="pt", truncation=True)
    translated = model.generate(**inputs, max_length=10)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def camel_case_split(identifier):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1 \2', identifier)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', s1)

def aggiungi_label_lxml(input_path, output_path):
    # Carica RDF con rdflib (opzionale, per controlli)
    g = Graph()
    g.parse(input_path, format="xml")

    # Leggi e modifica con lxml
    parser = ET.XMLParser(remove_blank_text=True)
    tree = ET.parse(input_path, parser)
    root = tree.getroot()

    ns = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#"
    }

    for elem in root.xpath(".//owl:Class | .//owl:ObjectProperty | .//owl:DatatypeProperty", namespaces=ns):
        about = elem.get("{%s}about" % ns["rdf"])
        if not about:
            continue

        existing_labels = elem.xpath("rdfs:label", namespaces=ns)
        existing_langs = {lab.attrib.get("{http://www.w3.org/XML/1998/namespace}lang") for lab in existing_labels}

        local_name = about.split("#")[-1] if "#" in about else about.split("/")[-1]
        label_en_raw = camel_case_split(local_name).strip()
        label_en = label_en_raw.title() if elem.tag.endswith("Class") else label_en_raw.lower()
        label_it = traduci_termine(label_en)

        if "en" not in existing_langs:
            label_elem = ET.SubElement(elem, "{%s}label" % ns["rdfs"])
            label_elem.set("{http://www.w3.org/XML/1998/namespace}lang", "en")
            label_elem.text = label_en

        if "it" not in existing_langs:
            label_elem = ET.SubElement(elem, "{%s}label" % ns["rdfs"])
            label_elem.set("{http://www.w3.org/XML/1998/namespace}lang", "it")
            label_elem.text = label_it

    tree.write(output_path, pretty_print=True, xml_declaration=True, encoding="utf-8")

# === ESECUZIONE ===
input_file = "archival-resource.owl"
output_file = "archival-resource_labeled_preservato.owl"
aggiungi_label_lxml(input_file, output_file)
