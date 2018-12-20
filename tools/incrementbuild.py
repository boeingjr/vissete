#!/usr/bin/env python
import re
import os
import sys

REPO_DIR=os.path.abspath(os.path.dirname(sys.argv[0]))[:-6]

if not os.path.exists("{}/Vissete".format(REPO_DIR)):
    print "Didn't find Vissete in {},\nplease ensure you invoke this script from the repository root directory.".format(REPO_DIR)
    sys.exit()

patternI = re.compile('.*bld=(.*)')

with open("{}/Vissete/Makefile".format(REPO_DIR), "r") as F:
    allLines = F.readlines()
    F.close()
    F = open("{}/Vissete/Makefile".format(REPO_DIR), "w")
    for line in allLines:
        if patternI.match(line):
            ss = patternI.search(line)
            bb = ss.group(1);
            BB = int(bb) + 1
            print "Updating {}/Vissete/Makefile to use build number {}".format(REPO_DIR, BB)
            F.write('bld={}\n'.format(BB))
        else:
            F.write(line)
    F.close()

