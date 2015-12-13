
with open('sample-line', 'r') as myfile:
    data=myfile.read()

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
        before_decimal = line[88:91].lstrip("0")
        print "before decimal: " + before_decimal
        # combine into string that can be cast to decimal
        degrees = sign + before_decimal + "." + line[91]
        print "Place 91: " + line[91]
        if (is_number(degrees)):
            if (float(degrees) < 618):
                return float(degrees)
            else:
                return 0
        else:
            return 0

print ('Max = %.1f' % mapper(data))
