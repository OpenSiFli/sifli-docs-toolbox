# SiFli Documentation Toolbox for Sphinx

## Usage
After installing the package, run `sf-build-docs` to build the document in the document root folder (in the same folder as `version.json`). The document source files need to be structured as below 
```
.
|
├── source
│   ├── _static
│   │   
│   ├── _templates
|   |
│   ├── assets
|   |
│   ├── en
│   │   ├── conf.py
│   │   └── index.md
│   └── zh_CN
│       ├── conf.py
│       └── index.md
├── .gitignore
|
└── version.json
```

You can also get a template document by cloning https://github.com/opensifli/sifli-doc-template/.

