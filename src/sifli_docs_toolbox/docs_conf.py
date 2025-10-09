# -*- coding: utf-8 -*-
# 
#  SPDX-FileCopyrightText: 2025 SiFli Technologies(Nanjing) Co., Ltd
# 
#  SPDX-License-Identifier: Apache-2.0
# 
#
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime
from pathlib import Path

author = 'SiFli'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              "myst_parser", 
              "sphinx_copybutton",
              "sphinx.ext.intersphinx",
              "sphinx_design",
              "sphinx_selective_exclude.eager_only",
              "sphinx_selective_exclude.search_auto_exclude",
              "sphinx_last_updated_by_git",
              "sphinx_simplepdf",
]

if 'simplepdf' in sys.argv:
    # only include gen_unique_ids extension when simplepdf builder is runs
    extensions +=  ["sifli_docs_toolbox.extensions.gen_unique_ids"]

templates_path = ['../_templates']
exclude_patterns = []
version = os.environ.get('SIFLI_DOC_VERSION', 'latest')
git_last_updated_timezone = 'Asia/Shanghai'
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'

current_year = datetime.datetime.now().year
language = os.environ.get('SIFLI_DOC_LANGUAGE', 'zh_CN')
if language == 'en':
    copyright = '2019 - {} SiFli Technologies(Nanjing) Co., Ltd.'.format(current_year)
else:
    copyright = '2019 - {} 思澈科技（南京）有限公司'.format(current_year)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['../_static']

html_context = {
    "versions": [
        ("latest", "/latest"),
        # 只保留latest版本，其他版本通过JavaScript动态加载
    ],
    "languages": [
        ("English", f"./{version}/en/%s/", "en"),
        ("中文", f"./{version}/zh_CN/%s/", "zh_CN"),
    ],
    "current_version": version,
    "curr_date": datetime.datetime.now().strftime("%Y-%m-%d")
}

docs_toolbox_dir = os.path.abspath(os.path.dirname(__file__))

html_logo = os.path.join(docs_toolbox_dir, '_static/logo_white.png')
html_favicon = os.path.join(docs_toolbox_dir, '_static/logo_favicon.png')
html_show_sourcelink = False

html_theme_options = {
    "accent_color": "blue",
    "feedback_disabled": False
}

# -- Options for myst_parser ----------------------------------------------------

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 6

simplepdf_vars = {
    'primary-opaque': 'rgba(31, 177, 170, 0.5)',
    'primary': '#1fb1aa',
    'secondary': '#961a1a',
    'cover': '#000000',
    'cover-bg': '#ffffff',
    'white': '#ffffff',
    'links': '#961a1a'
}

simplepdf_theme_options = {
    'custom_header': True,
    'custom_footer': True,
    'cover_sifli': True,
    'logo': '_static/logo_white_pdf.png',
    'website': 'www.sifli.com'

}

def setup(app):
    static_dir = Path(__file__).parent / "_static"

    if 'simplepdf' in sys.argv:
        is_simplepdf_builder = True
    else:
        is_simplepdf_builder = False

    app.config.html_static_path.append(str(static_dir))

    if is_simplepdf_builder:
        app.add_css_file("pdf.css")

    app.add_config_value('doc_id', None, 'env')
    app.add_config_value('chip', None, 'env')
    app.add_config_value('doc_name', None, 'env')
    app.add_config_value('pdf_url_enabled', None, 'env')
    app.add_config_value('doc_dir', None, 'env')

    app.connect('config-inited',  update_config)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

def update_config(app, config):
    if 'simplepdf' in sys.argv:
        is_simplepdf_builder = True
    else:
        is_simplepdf_builder = False

    if app.config.doc_id and app.config.chip and app.config.doc_name:
        pdf_filename = f"{app.config.doc_id}_{app.config.chip}_{app.config.doc_name}_{version}.pdf"
    else:
        pdf_filename = f"{app.config.project}.pdf"

    if is_simplepdf_builder and pdf_filename:
        app.config.simplepdf_file_name = pdf_filename

    if app.config.pdf_url_enabled:        
        doc_path = f'{app.config.doc_dir}/{app.config.version}/{language}/{pdf_filename}'
        html_theme_options['pdf_url'] = f"https://docs.sifli.com/projects/{doc_path}"


