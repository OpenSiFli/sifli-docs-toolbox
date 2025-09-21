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

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime

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
]

templates_path = ['../_templates']
exclude_patterns = []
version = os.environ.get('SIFLI_DOC_VERSION', 'latest')
git_last_updated_timezone = 'Asia/Shanghai'
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'

current_year = datetime.datetime.now().year
language = os.environ.get('SIFLI_DOC_LANGUAGE', 'zh_CN')
if language == 'en':
    copyright = '2019 - {} SiFli Technologies(Nanjing) Co., Ltd'.format(current_year)
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
}

html_logo = '../_static/logo_white.png'
html_favicon = '../_static/logo_favicon.png'
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




