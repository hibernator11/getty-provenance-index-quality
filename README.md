## Getty Provenance Index
This repository intends to describe examples of SPARQL queries for the [Provenance Index](https://data.getty.edu/provenance/docs/) at Getty. The SPARQL point is available at https://data.getty.edu/provenance/sparql-ui.


## Examples of SPARQL queries

### Retrieve all classes

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT distinct ?class WHERE {
  ?sub rdf:type ?class .
} LIMIT 100
```

### Retrieve places using Getty identifiers
```
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?getty ?label WHERE {
  ?sub rdf:type <http://www.cidoc-crm.org/cidoc-crm/E53_Place> .
  ?sub skos:exactMatch ?getty .
  ?sub rdfs:label ?label
} LIMIT 200
```

### Retrieve labels for the property cidoc:E10_Transfer_of_Custody

```
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT distinct ?label WHERE {
  ?sub rdf:type cidoc:E10_Transfer_of_Custody .
  ?sub rdfs:label ?label
} LIMIT 200
```

### Exploring how the Person class is used

```
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
  <https://data.getty.edu/provenance/a9d2c963-7a19-3a11-91e5-beb737d03c8a> rdf:type cidoc:E21_Person .
  <https://data.getty.edu/provenance/a9d2c963-7a19-3a11-91e5-beb737d03c8a> ?p ?obj
} LIMIT 200
```

### Explore how linguistic objects are described
```
SELECT *
WHERE {
    <https://data.getty.edu/provenance/e95701a5-2c7e-3d3e-b226-2da9fa1ca0e4> ?p ?obj
}
```

### Explore the labels describing the [provenance activities](https://observablehq.com/d/5c732aafeeb3134e)
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select distinct ?label
where { ?s rdf:type cidoc:E7_Activity . ?s rdfs:label ?label}
limit 5000
```

### Licence
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />Content is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International license</a>.

Please, note that the datasets used in this project have separate licences.

### References
- https://www.moma.org/collection/provenance/
- https://www.getty.edu/projects/getty-provenance-index-initiative/research-inspired-by-the-getty-provenance-index/
- https://www.getty.edu/databases-tools-and-technologies/provenance/
- https://vocab.getty.edu/tgn/
- https://observablehq.com/d/6c4d0f0ff448a165
- https://www.openartdata.org/2025/10/dataset-getty-gpi-merged-with-wikidata.html?m=1
