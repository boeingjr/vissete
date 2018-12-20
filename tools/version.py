#!/usr/bin/env python
import re
import os
import sys

REPO_DIR=os.path.abspath(os.path.dirname(sys.argv[0]))[:-6]

if not os.path.exists("{}/Vissete".format(REPO_DIR)):
    print "Didn't find Vissete in {},\nplease ensure you invoke this script from the repository root directory.".format(REPO_DIR)
    sys.exit()

patternI = re.compile('.*vrsn=.*')
patternVersion = re.compile('([0-9]+)\.([0-9]+)\.([0-9]+)')
argVersion = None

for arg in sys.argv:
    if patternVersion.match(arg):
        argVersion = arg
    elif not arg == sys.argv[0]:
        print "WARNING! Ignoring unrecognized argument: {}".format(arg)

if argVersion == None:
    print "ERROR! No version specified!"
    sys.exit()
elif argVersion == "0.0.0":
    print "ERROR! No version specified!"
    sys.exit()

print "Updating {}/Vissete/Makefile to use version number {}".format(REPO_DIR, argVersion)

with open("{}/Vissete/Makefile".format(REPO_DIR), "r") as F:
    allLines = F.readlines()
    F.close()
    F = open("{}/Vissete/Makefile".format(REPO_DIR), "w")
    for line in allLines:
        if patternI.match(line):
            F.write('vrsn={}\n'.format(argVersion))
        else:
            F.write(line)
    F.close()

