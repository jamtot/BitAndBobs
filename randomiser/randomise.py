"""returns a randomised list of objects in a text file"""

import sys
import random

def getnames(filename):
    with open(filename) as namefile:
        names = namefile.read().splitlines()
    return names

def getrand(to):
    return random.randint(0,to)

def randomise(names):
    amount = len(names)
    seq = [getrand(amount-1)]
    sofar = 1
    while sofar < amount:
        randnum = getrand(amount-1)
        if randnum not in seq:
            seq.append(randnum)
            sofar+=1
    return seq

def writefile(filename, names, seq, number):
    with open(filename, 'w') as newfile:
        i = 1
        for n in seq:
            prefix = ''
            if number:
                prefix = str(i)
                if filename.endswith(".csv"):
                    prefix+=','
                else: prefix+=' '
                i+=1
            newfile.write(prefix+names[n]+'\n')

if __name__ == "__main__":
    number_file = False
    try:
        number_file = sys.argv[3] == 'True'
    except IndexError:
        pass # file not being numbered, nothing entered
    try:
        names = getnames(sys.argv[1])
        seq = randomise(names)
        writefile(sys.argv[2], names, seq, number_file) 
    except IndexError:
        print "Enter textfile input and output names."
    except IOError:
        print "That file does not exist."
