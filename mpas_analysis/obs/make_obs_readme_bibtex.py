#!/usr/bin/env python
# Copyright (c) 2017,  Los Alamos National Security, LLC (LANS)
# and the University Corporation for Atmospheric Research (UCAR).
#
# Unless noted otherwise source code is licensed under the BSD license.
# Additional copyright and license information can be found in the LICENSE file
# distributed with this code, or at http://mpas-dev.github.com/license.html
#

"""
This script is used to automatically generate a README.md file describing each
set of observations in the observtional_datasets.xml along with obs.bib,
containing bibtex entries for related papers or reports.

Xylar Asay-Davis
"""

from __future__ import absolute_import, division, print_function, \
    unicode_literals

import xml.etree.ElementTree as ET
import argparse
import re
import os


def spurious_newline_whitespace(data):
    whitespace = re.findall('\n\s*', data)
    if len(whitespace) > 0:
        astr = min(whitespace)
        data = data.replace(astr, "\n")
    return data


def cleanup(linedata):
    cleanups = [spurious_newline_whitespace]
    for acleanup in cleanups:
        linedata = acleanup(linedata)
    return linedata


def build_readmes(xmlFile, outDir):

    # open xml file for reading
    xml = ET.parse(xmlFile)

    titles = {'description': 'Description',
              'source': 'Source',
              'releasePolicy': 'Release Policy',
              'references': 'References',
              'tasks': 'MPAS-Analysis Tasks'}

    for entry in xml.findall('observation'):
        name = entry.findall('name')[0].text.strip()
        subdirectory = entry.findall('subdirectory')
        if len(subdirectory) == 0:
            print('Warning: {} has no subdirectory tag'.format(name))
            continue
        subdirectory = subdirectory[0].text.strip()
        path = '{}/{}'.format(outDir, subdirectory)
        try:
            os.makedirs(path)
        except OSError:
            pass

        readme = open('{}/README.md'.format(path), 'w')

        readme.write('{}\n'.format(name))
        readme.write('='*len(name))
        readme.write('\n\n')

        for tag in titles:
            title = titles[tag]
            readme.write('{}\n'.format(title))
            readme.write('{}\n'.format('-'*len(title)))
            text = cleanup(entry.findall(tag)[0].text.strip())
            readme.write('{}\n\n'.format(text))
        readme.close()


def build_bibtex(xmlFile, outDir):

    # open xml file for reading
    xml = ET.parse(xmlFile)

    for entry in xml.findall('observation'):
        name = entry.findall('name')[0].text.strip()
        subdirectory = entry.findall('subdirectory')
        if len(subdirectory) == 0:
            print('Warning: {} has no subdirectory tag'.format(name))
            continue
        subdirectory = subdirectory[0].text.strip()
        path = '{}/{}'.format(outDir, subdirectory)
        try:
            os.makedirs(path)
        except OSError:
            pass

        saved = False
        bibtex = entry.findall('bibtex')
        if len(bibtex) > 0:
            text = cleanup(bibtex[0].text.strip())
            if len(text) > 0:
                saved = True
                with open('{}/obs.bib'.format(path), 'w') as bibtexFile:
                    bibtexFile.write('{}\n'.format(text))
        if not saved:
            print('Warning: no bibtex for {}'.format(name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-o", "--outDir", dest="outDir",
                        help="Base output directory containing observations",
                        metavar="OBS_DIR", required=True)

    args = parser.parse_args()

    xmlFile = 'observational_datasets.xml'

    build_readmes(xmlFile, args.outDir)
    build_bibtex(xmlFile, args.outDir)
