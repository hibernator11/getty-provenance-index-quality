#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 08:51:31 2026

@author: gustavo
"""

from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
    "http://www.cidoc-crm.org/cidoc-crm/E8_Acquisition",
    "http://www.cidoc-crm.org/cidoc-crm/E7_Activity",
    "http://www.cidoc-crm.org/cidoc-crm/E98_Currency",
    "https://linked.art/ns/terms/Payment",
    "http://www.cidoc-crm.org/cidoc-crm/E97_Monetary_Amount",
    "http://www.ics.forth.gr/isl/CRMdig/D1_Digital_Object",
    "http://www.ics.forth.gr/isl/CRMsci/S19_Encounter_Event",
    "http://www.cidoc-crm.org/cidoc-crm/E55_Type",
    "http://www.cidoc-crm.org/cidoc-crm/E33_E41_Linguistic_Appellation",
    "http://www.cidoc-crm.org/cidoc-crm/E36_Visual_Item",
    "http://www.cidoc-crm.org/cidoc-crm/E33_Linguistic_Object",
    "http://www.cidoc-crm.org/cidoc-crm/E53_Place",
    "http://www.cidoc-crm.org/cidoc-crm/E69_Death",
    "http://www.cidoc-crm.org/cidoc-crm/E67_Birth",
    "http://www.cidoc-crm.org/cidoc-crm/E10_Transfer_of_Custody",
    "http://www.cidoc-crm.org/cidoc-crm/E66_Formation",
    "http://www.cidoc-crm.org/cidoc-crm/E39_Actor",
    "http://www.cidoc-crm.org/cidoc-crm/E58_Measurement_Unit",
    "http://www.cidoc-crm.org/cidoc-crm/E30_Right",
    "https://linked.art/ns/terms/RightAcquisition",
    "http://www.cidoc-crm.org/cidoc-crm/E54_Dimension",
    "http://www.cidoc-crm.org/cidoc-crm/E13_Attribute_Assignment",
    "http://www.cidoc-crm.org/cidoc-crm/E42_Identifier",
    "http://www.cidoc-crm.org/cidoc-crm/E65_Creation",
    "http://www.cidoc-crm.org/cidoc-crm/E74_Group",
    "http://www.cidoc-crm.org/cidoc-crm/E21_Person",
    "http://www.cidoc-crm.org/cidoc-crm/E12_Production",
    "http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span",
    "http://www.cidoc-crm.org/cidoc-crm/E22_Human-Made_Object",
    "http://www.cidoc-crm.org/cidoc-crm/E68_Dissolution",
    "http://www.cidoc-crm.org/cidoc-crm/E6_Destruction",
    "http://www.cidoc-crm.org/cidoc-crm/E57_Material",
    "http://www.cidoc-crm.org/cidoc-crm/E56_Language",
    "http://www.cidoc-crm.org/cidoc-crm/E19_Physical_Object",
    "https://linked.art/ns/terms/Set",
    "http://www.cidoc-crm.org/cidoc-crm/E70_Thing",
    "http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity",
    "https://www.w3.org/2004/03/trix/rdfg-1/Graph"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://www.cidoc-crm.org/cidoc-crm/": "cidoc-crm",
                   "http://schema.org/": "schema",
                   "http://rdfs.org/ns/void#": "void",
                   "http://creativecommons.org/ns#": "creativeCommons",
                   "http://purl.org/dc/terms/": "dc",
                   "http://www.w3.org/2003/01/geo/wgs84_pos#": "geo",
                   "http://purl.org/ontology/bibo/": "bibo",
                   "https://linked.art/ns/terms/": "art"
                   }

url_endpoint="https://data.getty.edu/provenance/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=NT,
                limit_remote_instances=100,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_getty_provenance.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")

