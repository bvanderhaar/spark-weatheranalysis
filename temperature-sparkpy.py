
from __future__ import print_function

import sys
import math
from operator import add
from pyspark import SparkContext

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def mapper(line):
        # positive or negative
        sign = line[87:88]
        # before the decimal point, remove leading zeros
        before_decimal = line[88:92].lstrip("0")
        # combine into string that can be cast to decimal
        degrees = sign + before_decimal + "." + line[92:93]
        if (is_number(degrees)):
            if (float(degrees) < 618):
                return float(degrees)
            else:
                return 0
        else:
            return 0

def reducer(a, b):
    if a > b:
        return a
    else:
        return b

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="PySparkTemperature")
    lines = sc.textFile(sys.argv[1], 1)
    output = lines.map(mapper) \
                  .reduce(reducer)

    print ('Max = %.1f' % output)

    sc.stop()
