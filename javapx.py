import os
import re
import sys

name_code = {}

path = os.path.realpath(__file__)
path = os.path.dirname(path)
path = os.path.join(path, "bytecode.txt")

with open(path) as fp:
    for line in fp:
        if line.startswith("#"):
            continue
        (name, code) = line.split("\t")
        name_code[name] = code.rstrip()

p = re.compile('^(\s+)(\d+)(:\s)(\w+)(\s.*)$')

#with open() as fp:
for line in sys.stdin:
    m = p.match(line)
    if m is None:
        print line,
    else:
        print m.groups()[0],
        print m.groups()[1],
        print m.groups()[2],
        if m.groups()[3] not in name_code:
            raise Exception("Op name {0} is unknown. Google it and add to bytecode.txt".format(m.groups()[3]))
        print "{0} ({1})".format(m.groups()[3], name_code[m.groups()[3]]),
        print m.groups()[4]
