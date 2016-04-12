d = {"Illinois": ['13', '12', '18', '23', '26', '25', '24', '19', '13', '10', '15', '14', '14', '4', '3'],
"Indiana": ['7', '6', '7', '8', '11', '11', '13', '12', '7', '7', '7', '7', '9', '2', '2']}

if __name__ == "__main__":
    print d

    for state in d:
        # returns the numbers with their index (#, index)
        pairs = [(int(d[state][x]), x) for x in xrange(len(d[state]))]
        minpair = min(pairs)
        maxpair = max(pairs)
        print "%s: %d in index %d and %d in index %d"%(state,maxpair[0],maxpair[1],
        minpair[0],minpair[1])


#output
"""
{'Indiana': ['7', '6', '7', '8', '11', '11', '13', '12', '7', '7', '7', '7', '9', '2', '2'], 'Illinois': ['13', '12', '18', '23', '26', '25', '24', '19', '13', '10', '15', '14', '14', '4', '3']}
Indiana: 13 in index 6 and 2 in index 13
Illinois: 26 in index 4 and 3 in index 14
"""
