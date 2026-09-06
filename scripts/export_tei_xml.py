#!/usr/bin/env python3
"""
Exports el-mehasin-vel-ezdad dialectic corpus to TEI XML (Text Encoding Initiative).
"""
import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def export_tei_xml(input_path="data/dialectic_pairs.jsonl", output_path="data/corpus_tei.xml"):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    root = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
    
    # Header
    teiHeader = ET.SubElement(root, "teiHeader")
    fileDesc = ET.SubElement(teiHeader, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    title = ET.SubElement(titleStmt, "title")
    title.text = "Kitab al-Mahasin wa-al-Addad: Digital Humanities Dialectic Corpus"
    author = ET.SubElement(titleStmt, "author")
    author.text = "Pseudo-Jahiz / Ibrahim b. Muhammad al-Bayhaqi"

    # Body
    text_elem = ET.SubElement(root, "text")
    body = ET.SubElement(text_elem, "body")

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            item = json.loads(line)
            div = ET.SubElement(body, "div", type="dialectic_pair", id=item["entry_id"])
            head = ET.SubElement(div, "head")
            head.text = item["classical_arabic_title"]

            # Thesis
            t_div = ET.SubElement(div, "div", type="thesis", pole="mehasin")
            t_head = ET.SubElement(t_div, "head")
            t_head.text = item["thesis"]["concept"]
            t_premise = ET.SubElement(t_div, "p", type="premise")
            t_premise.text = item["thesis"]["core_premise"]
            t_q = ET.SubElement(t_div, "quote", lang="ar")
            t_q.text = item["thesis"]["top_quote"]["arabic"]

            # Antithesis
            a_div = ET.SubElement(div, "div", type="antithesis", pole="ezdad")
            a_head = ET.SubElement(a_div, "head")
            a_head.text = item["antithesis"]["concept"]
            a_premise = ET.SubElement(a_div, "p", type="premise")
            a_premise.text = item["antithesis"]["core_premise"]
            a_q = ET.SubElement(a_div, "quote", lang="ar")
            a_q.text = item["antithesis"]["top_quote"]["arabic"]

            # Synthesis
            syn = ET.SubElement(div, "div", type="synthesis")
            syn_p = ET.SubElement(syn, "p")
            syn_p.text = item["dialectic_synthesis"]

    xml_str = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="  ")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print(f"Successfully exported TEI XML to {output_path}")

if __name__ == "__main__":
    export_tei_xml()
