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
import sys
import argparse

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

def get(name, filename):
    """ Gets a snippet with an associated name in the CSV file """
    logging.info('Retrieving {!r} from {!r}'.format(name, filename))
    logging.debug('Opening file')
    with open(filename, 'rb') as s:
        reader = csv.reader(s)
        logging.debug('Retrieving snippet from file')
        for row in reader:
                if row[0] == name:
                    logging.debug('Retrieved sucessful')
                    return row
                else:
                    logging.debug('Retrieved failed')
                    return False

def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")
    get_parser = subparsers.add_parser("get", help="retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")

    return parser

def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}".format(snippet, name)

    if command == "get":
        name = get(**arguments)
        #print "Retrieved {!r} from {!r}".format(snippet, name)
        if name is not False:
            print "Retrieved {!r} from {!r}".format(name[0], name[1])
        else:
            print('Could not be found')
            sys.exit(1)

if __name__ == "__main__":
    main()
