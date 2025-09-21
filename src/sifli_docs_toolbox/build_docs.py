#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#  SPDX-FileCopyrightText: 2025 SiFli Technologies(Nanjing) Co., Ltd
# 
#  SPDX-License-Identifier: Apache-2.0
# 

import subprocess
import argparse
import os
import shutil


def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error executing {command}")
        exit(result.returncode)


def make_html(version, lang):
    print(f"Building HTML documentation for version {version}, language: {lang} ...")
    if version:
        os.environ['SIFLI_DOC_VERSION'] = version
    os.environ['SIFLI_DOC_LANGUAGE'] = lang
    run_command(f'sphinx-build -M html source/{lang} build/{lang} -j 8')


def _main(version, lang):
    make_html(version, lang)

def main():
    parser = argparse.ArgumentParser(description='Generate documentation.')
    parser.add_argument('--lang', choices=['en', 'zh_CN'], default='zh_CN', help='Specify language(en or zh_CN)')
    parser.add_argument('--version', type=str, help='Specify version')
    args = parser.parse_args()

    _main(args.version, args.lang)

if __name__ == "__main__":
    main()