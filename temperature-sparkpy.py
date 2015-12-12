
from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext

def mapper(line):
        # positive or negative
        sign = line[87:88]
        # before the decimal point, remove leading zeros
        before_decimal = line[88:92].lstrip("0")
        # combine into string that can be cast to decimal
        degrees = sign + before_decimal + "." + line[92:93]
        return float(degrees)

#def reducer(x,y):
#        return x+y

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="PySparkTemperature")
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(mapper) \
                  .reduce(Math.max)
    output = counts.collect()
    print ("Max " + output)

    sc.stop()
