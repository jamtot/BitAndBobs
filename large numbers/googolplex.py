import time

def bypowers():
    start = time.time()
    googol = 10**100
    googolplex = 10**googol
    
    with open("gplex1.txt", "w") as gfile:
        gfile.write("Googol:\n%r\n" % googol)
        gfile.write("Googolplex:\n%r" % googolplex)
        gfile.write("This took %r secs to compute." % (time.time() - start))


def bystringiter():
    start = time.time()
    with open("gplex2.txt", "w") as gfile:
        googol = 10**100
        gfile.write("Googol:\n%r\n" % googol)
        gfile.write("Googolplex:\n")
        gfile.write("1")
        i = 0 
        tenzeros = "0"*10
        top = googol/10
        while i < top:
            gfile.write(tenzeros)
            i+=1
        gfile.write("\nThis too %r secs to compute." % (time.time() - start))   

if __name__ == "__main__":
    # maybe some day I'll be able to run something like this
    # apparently will take about 3.867 x 10^90 gbs of space to print
    # there are 10^80 particles in the universe
    bypowers()
    bystringiter()
