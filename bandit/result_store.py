#!/usr/bin/env python

"""An object to store/access results associated with Bandit tests."""

from collections import OrderedDict
import linecache
from sys import stdout

import utils

class BanditResultStore():
    resstore = OrderedDict()
    count = 0

    def __init__(self, logger):
        self.count = 0
        self.logger = logger

    def add(self, file_detail, issue_type, issue_text):
        filename, lineno = file_detail
        if filename in self.resstore:
            self.resstore[filename].append((lineno, issue_type, issue_text))
        else:
            self.resstore[filename] = [(lineno, issue_type, issue_text),]
        self.count += 1

    def report(self, scope, lines=0, level=1, is_tty=stdout.isatty()):
        if level >= len(utils.sev):
            level = len(utils.sev) - 1
        tmpstr = ""
        if self.count > 0:
            tmpstr += "%sFiles tested (%s):%s\n\t" % (utils.color['HEADER'], len(scope), utils.color['DEFAULT']) if is_tty else "File tested (%s):\n\t" % (len(scope))

            tmpstr += "%s\n" % "\n\t".join(scope)
            tmpstr += "%sTest results:%s\n" % (utils.color['HEADER'], utils.color['DEFAULT']) if is_tty else "Test results:\n"

            for filename,issues in self.resstore.items():
                for lineno, issue_type, issue_text in issues:
                    if utils.sev.index(issue_type) >= level:
                        tmpstr += "%s>> %s\n - %s::%s%s\n" % (utils.color.get(issue_type, utils.color['DEFAULT']), issue_text, filename, lineno, utils.color['DEFAULT']) if is_tty else ">> %s\n - %s::%s\n" % (issue_text, filename, lineno)
                        for i in utils.mid_range(lineno, lines):
                            line = linecache.getline(filename, i)
                            #linecache returns '' if line does not exist
                            if line != '':
                                tmpstr += "\t%3d  %s" % (i, linecache.getline(filename, i))
            print(tmpstr)
        else:
            self.logger.error("no results to display - %s files scanned" % self.count)

