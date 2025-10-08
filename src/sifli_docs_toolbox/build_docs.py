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

docs_toolbox_dir = os.path.abspath(os.path.dirname(__file__))

def copy_static_files():
    static_src = os.path.join(docs_toolbox_dir, '_static')
    static_dst = os.path.join('source', '_static')

    print(static_src)

    if not os.path.exists(static_dst):
        os.makedirs(static_dst)

    for root, _, files in os.walk(static_src):
        for file in files:
            src_file = os.path.join(root, file)
            relative_path = os.path.relpath(src_file, static_src)
            dst_file = os.path.join(static_dst, relative_path)
            print(src_file)
            print(dst_file)

            dst_dir = os.path.dirname(dst_file)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

            if not os.path.exists(dst_file):
                shutil.copy2(src_file, dst_file)


def run_command(command, cwd=None):
    print(f"Run command: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error executing {command}")
        exit(result.returncode)


def make_doc(version, lang, is_pdf, non_clean):
    if is_pdf:
        print(f"Building PDF documentation for version {version}, language: {lang} ...")
    else:
        print(f"Building HTML documentation for version {version}, language: {lang} ...")
    if version:
        os.environ['SIFLI_DOC_VERSION'] = version
    os.environ['SIFLI_DOC_LANGUAGE'] = lang
    if not non_clean:
        opts = '-a -E'
    else:
        opts = ''

    if is_pdf:
        run_command(f'sphinx-build -M simplepdf source/{lang} build/{lang} {opts} -j 8')
    else:
        run_command(f'sphinx-build -M html source/{lang} build/{lang} {opts} -j 8')

def _main(version, lang, pdf, non_clean):
    make_doc(version, lang, pdf, non_clean)

def main():
    parser = argparse.ArgumentParser(description='Generate documentation.')
    parser.add_argument('--lang', choices=['en', 'zh_CN'], default='zh_CN', help='Specify language(en or zh_CN)')
    parser.add_argument('--version', type=str, help='Specify version')
    parser.add_argument('--pdf', action="store_true", help='Build PDF')
    parser.add_argument('--non-clean', action="store_true", help='non clean build')
    args = parser.parse_args()

    _main(args.version, args.lang, args.pdf, args.non_clean)

if __name__ == "__main__":
    main()