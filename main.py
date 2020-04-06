#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
# Copyright: (c) 2020, Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import argparse
import os

try:
    import argcomplete
except ImportError:
    argcomplete = None


def parse_args():
    parser = argparse.ArgumentParser(
        description='Autogenerate modules from OpenAPI file'
    )

    # Debug
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='Show all debug logs')

    if argcomplete:
        argcomplete.autocomplete(parser)

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    product_dir = "./products/petstore"
    product_file = os.path.join(product_dir, 'petstore-simple.json')

    if os.path.exists(product_file):
        print("Reading %s" % product_file)

    

if __name__ == '__main__':
    main()