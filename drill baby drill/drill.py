def divisby(fr=1, to=1000, n=7): # or just count up in 7s
    return [i for i in xrange(fr, to+1) if i%n == 0]

def numwith(fr=1, to=1000, n=3):
    return [i for i in xrange(fr, to+1) if str(n) in str(i)]

def spaces(string, char=' '):
    return sum([1 for l in string if l == char])

def remove(string, removey="aeiouAEIOU"):
    return "".join([l for l in string if l not in removey])

def findwordslessthan(string, size=4):
    return [word for word in string.split() if len(word) < size]

# neither take into account punctuation
def wordnlengths(string): # returns dictionary
    lendict = {}
    for word in string.split(): lendict[word] = len(word)
    return lendict
# or
def wordlengths(string): # returns list
    return [len(word) for word in string.split()]

def divisbynums(fr=1, to=1000, nums=range(2,10)):
    numlist= []
    for i in xrange(fr, to+1): 
        if any(not (i%num) for num in nums): 
            numlist+=[i]
    return numlist

# very brute-force-y
def highestdiv(fr=1, to=1000, digs=range(9,0,-1)):
    numdict = {}
    for i in xrange(fr,to+1):
        for d in digs:
            if i%d==0:
                numdict[i]=d
                break
    return numdict

if __name__ in "__main__":
    print divisby()
    print numwith()
    print spaces("Hello, World! How are you?")
    print remove("Hello, World! How are you?")
    print findwordslessthan("Hello, World! How are you?")
    print wordnlengths("Hello, World! How are you?")
    print wordlengths("Hello, World! How are you?")
    print divisbynums()
    print highestdiv()
