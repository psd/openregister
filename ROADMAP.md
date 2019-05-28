Features prioritised for [digital land](https://gitub.io/digital-land)

* single register routes:
  - /register
  - /records
  - /records/{key}
  - /records/{key}/entries
  - /entries/{entry-number}
  - /entries/
  - /items/
  - /items/{item-hash}
  - /download

* multiple register (catalog?) routes:
  - /registers
  - /items/
  - /registers/{register}/ (single register routes)

* vanilla HTML views for all routes (essential!)

* multiple representations for data (for all of the above routes):
  - .json
  - .jsonl
  - .csv
  - .tsv
  - .yaml
  - .txt
  - .ttl
  - .geojson

* external data sources
  - mirror an external GOV.UK register [mirror.py](/mirror.py)
  - seed entries from a CSV file (needed for prototyping registers)
  - pull entries and items from trusted sources (editor platforms)

* link headers, etc
  - favicon
  - machine friendly robots.txt
  - content-security-policy
  - CORS

* indexing
  - cross-reference
  - text searching
  - spatial searching, items within a boundary or bounding box

* implement more stores for Heroku etc:
  - sqlite store
  - spatialite indexes

* implement missing entry features:
  - support insertion of an older entry
  - support correction of an older entry
  - support redaction of an older entry in extremis

* publish as:
  - Heroko, Ziet and Google Cloud Run application
  - a datasette index
  - static site (github.io etc)
  - frictionless data package

* plugin support using pluggy
   - refactor to make stores, representations, views, templates, publishers, etc extensible
   - support a GOV.UK theme

* project
  - make a release from TravisCI
  - freeze badges and links in release [PyPI description](https://pypi.org/project/openregister/)
  - move ROADMAP to GitHub issues

* restore original routes (maybe)
   - redirect /entries/{entry} to /entry/{entry} etc
   - hypermedia /download-register linking to /archive.zip
