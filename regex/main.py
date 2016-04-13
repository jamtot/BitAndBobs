import re

def atbash(string):
    offset = ord('a')
    string = re.sub("[a-z]", lambda x: chr( (25-((ord(x.group(0))-offset))) +offset), string)
    offset = ord('A')
    string = re.sub("[A-Z]", lambda x: chr( (25-((ord(x.group(0))-offset))) +offset), string)
    print string


def exper():
    string = "Hello, my name is Jonathan."
    subbedstring = re.sub(r"[tn]", lambda x: x.group(0).upper(), string)
    print string
    print subbedstring
    
    subbedstring = re.sub(r"[HT]", lambda x: x.group(0).lower(), subbedstring)
    print subbedstring
    # changes case of found letters
    changecase = lambda x: x.group(0).upper() if x.group(0).islower()  else x.group(0).lower()
    subbedstring = re.sub(r"[A-Za-z]", changecase, subbedstring)
    print subbedstring

    
if __name__ == "__main__":
    exper()

    atbash("Gsrh rh zm Vcznkov lu gsv Zgyzhs Xrksvi")

