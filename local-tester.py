

with open('sample-line', 'r') as myfile:
    data=myfile.read()

def mapper(line):
        print "line: " + line
        # positive or negative
        sign = line[87:88]
        print "sign = " + sign
        # before the decimal point, remove leading zeros
        before_decimal = line[88:92].lstrip("0")
        print "before_decimal: " + before_decimal
        # combine into string that can be cast to decimal
        degrees = sign + before_decimal + "." + line[92:93]
        print "degrees: " + degrees
        return float(degrees)

print ('Max = %.1f' % mapper(data))
