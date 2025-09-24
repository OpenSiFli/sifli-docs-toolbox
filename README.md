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

## Download
The latest version could be found: 
- [wheel](https://downloads.sifli.com/tools/sifli-docs-toolbox/latest/sifli_docs_toolbox-latest-py3-none-any.whl)
- [source](https://downloads.sifli.com/tools/sifli-docs-toolbox/latest/sifli_docs_toolbox-latest.tar.gz)

Old version could be found:
- [v0.1.5](https://downloads.sifli.com/tools/sifli-docs-toolbox/v0.1.5/sifli_docs_toolbox-0.1.5-py3-none-any.whl)
- [v0.1.4](https://downloads.sifli.com/tools/sifli-docs-toolbox/v0.1.4/sifli_docs_toolbox-0.1.4-py3-none-any.whl)