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

`sf-build-docs`命令行参数：
- `--help`: 查看命令行参数说明
- `--lang`: 指定文档语言，缺省为中文
- `--version`: 指定文档版本号，缺省为`latest`
- `--pdf`: 生成PDF文档，缺省为生成HTML文档, Windows平台**不支持**PDF文档编译
- `--clean`: 清空编译，如果编译不同格式的文档需要选择清空编译，比如编译完PDF格式的文档想编译HTML，需要选择清空编译
- `--cores`: 指定并行编译使用的内核数量，缺省为8个

## Download
The latest version could be found: 
- [wheel](https://downloads.sifli.com/tools/sifli-docs-toolbox/latest/sifli_docs_toolbox-latest-py3-none-any.whl)
- [source](https://downloads.sifli.com/tools/sifli-docs-toolbox/latest/sifli_docs_toolbox-latest.tar.gz)

Old version could be found:
- [v0.1.5](https://downloads.sifli.com/tools/sifli-docs-toolbox/v0.1.5/sifli_docs_toolbox-0.1.5-py3-none-any.whl)
- [v0.1.4](https://downloads.sifli.com/tools/sifli-docs-toolbox/v0.1.4/sifli_docs_toolbox-0.1.4-py3-none-any.whl)


## 自定义配置
在文档项目的`conf.py`里可以使用如下变量对文档进行配置
- `doc_id`: 文档编号, 比如 `UM5202`、`RPT5202`
- `chip`: 芯片型号，比如 `SF32LB52x`
- `doc_name`: 文档名称，比如“用户手册”、“芯片规格书”、“功耗测试报告”等
- `pdf_url_enabled`: HTML文档是否需要放置PDF文档链接，`True`: 有链接
- `doc_dir`: 文档路径，比如在线文档的链接是`https://docs.sifli.com/projects/rpt5202_sf32lb52x-low-power-measurement-report/latest/zh_CN/index.html`，则`dor_dir`设置
为`rpt5202_sf32lb52x-low-power-measurement-report`

### PDF文件名规则
如果同时定义了`doc_id`、`chip`和`doc_name`三个变量，那么PDF文档名以`{doc_id}_{chip}_{doc_name}_{version}.pdf`格式命名，其中`version`为版本号，
否则以`{project}_{version}.pdf`格式命名，其中`project`也是在`conf.py`中定义的项目名称