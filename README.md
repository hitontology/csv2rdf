# HITO-CSV2RDF
Transformation of the HITO CSV tables to RDF/OWL

## Background

The HITO project contains catalogues of features and other things.
These catalogues are first extracted as CSV tables and then converted to RDF.
This repository contains the scripts used to convert CSV tables, that are created by domain experts working for SNIK.
After a catalogue is converted to RDF, it gets added to the HITO ontology repository and a copy is uploaded to the [HITO SPARQL Endpoint](http://www.hitontology.eu/sparql).
The repository is the source of truth and changes to the SPARQL endpoint are not permanent.
We are currently in the process of moving the source of truth for all software products and related attributes to a database, see https://github.com/hitontology/database.

## Attributes

You may describe software products both with an attribute.csv and a base.ttl file, though we recommend to use attribute.csv for all supported attributes and base.ttl for the rest. attribute.csv doesn't fit catalogues well, so we recommend just the base.ttl there.

## Requirements

* Linux
* installed [tarql](https://tarql.github.io/) and [rapper](http://librdf.org/raptor/rapper.html)

## Steps

1. Run `map`, if there is an error with your directory or the final test is not successful, fix the source files and run map again until it completes successfully.
2. Upload the resulting ntriples files (1 per directory/source) in the [HITO SPARQL endpoint conductor](https://www.snik.eu/conductor) (credentials required). Make sure to provide the correct graph name, such as http://hitontology.eu/ontology and to clear that graph first.
