#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: snippets
#   date: 2014-11-04
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

import logging
import csv

# set the log output file, and the log level.
logging.basicConfig(filename='output.log', level=logging.DEBUG)

def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info('Writing {!r}:{!r} to {!r}'.format(name, snippet, filename))
    logging.debug('Opening file')
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        logging.debug('Writing snippet to file')
        writer.writerow([name, snippet])
    logging.debug('Write sucessful')
    return name, snippet
