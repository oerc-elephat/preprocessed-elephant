# preprocessed-elephant
eeboo-ontology.ttl: An ontology in .ttl to map the classes and properties of those metadata entities as pulled out of the EEBO (Early English Books Online) phase1 XML records using the metadata-subset code.
metadata-subset.py: Used to pull out a small number of specific metadata entities from the XML files for EEBO (Early English Books Online)  phase1 XML records, such as author, publication place, publication year, title, and id numbers.
regex-author-year: regex used to tidy up and sort the dates as associated with the authors e.g. date of birth.
regex-publication-date: regex used to tidy up and sort publication dates for works.

We used the Karma Data Integration Tool to generated the RDF triples using various ontologies for bibliographic metadata. Karma is available from https://github.com/usc-isi-i2/Web-Karma/wiki/Installation.
We also used the MODS/RDF and MADS/RDF ontologies, available respectively from http://www.loc.gov/standards/mods/modsrdf/ and http://www.loc.gov/standards/mads/rdf/ .

The Karma mapping was completed in several steps, each in captured in a sepate .ttl files. 
WSP1WS1-karma-eeboo-data-final.csv-auto-model.ttl maps the generated data to the MADS/RDF, MODS/RDF and EEBOO ontologies.
WSP1WS2-eebo-person-viaf-lc-links.csv-auto-model.ttl maps the person identities from the data to VIAF and LOC ids as applicable.
WSP1WS2-final-author-dates.csv-auto-model.ttl maps author dates such as date of birth and date of death to the appropriate person.
WSP1WS2-final-publication-dates.csv-auto-model.ttl maps the publication dates to the appropriate work.
WSP1WS2-id-numbers-to-match-jisc.csv-auto-model.ttl maps work-identifiers to their equivalents in the JISC Historical Texts project equivalent, as at https://historicaltexts.jisc.ac.uk/home
WSP1WS3-raw-publication-place-and-imprint.csv-auto-model.ttl maps a untidied publication place and untidied imprint (publication) data to the appropriate work.
WSP1WS4-eebo-id-and-title.csv-auto-model.ttl maps one bibliographical ID number and the title of a work to the appropriate work.