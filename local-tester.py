from __future__ import print_function

import sys
from operator import add
from decimal import Decimal

with open('sample-line', 'r') as myfile:
    data=myfile.read()

def mapper(line):
        # positive or negative
        sign = line[88:1]
        # before the decimal point, remove leading zeros
        before_decimal = line[89:4].lstrip("0")
        # combine into string that can be cast to decimal
        degrees = sign + before_decimal + "." + line[93:1]
        return decimal.Decimal(degrees)

print (mapper(data))
