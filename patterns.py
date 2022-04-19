import math
import csv
import pandas as pd
import numpy as np
import itertools


# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE

    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]
    
    #first I guess we figure out how to pull all sets?

    #declare a set to store what we want to return (frequencies, after everything is empty)
    oldFrequencies = {}

    #track frequencies of things
    frequencies = {}

    #Look at every individual item first

    #for each itemset in the list of itemsets, do this
    for itemset in itemsets:
        #for each item in the itemset, do this
        for item in itemset:
            
            #if this item already exists in frequencies, increment; if not, make it and set it to 1
            if frozenset(item) in frequencies:
                frequencies[frozenset(item)] += 1
            else:
                frequencies[frozenset(item)] = 1


    print (frequencies)


    #divide every value inside of frequencies by numberOfItems to get support
    for item in list(frequencies.keys()):
        frequencies[item] = frequencies[item] / len(itemsets)
        #purge anything that has less frequency than our threshold
        if frequencies[item] < threshold:
            oldFrequencies[item] = frequencies.pop(item)

    print(frequencies)
    print(oldFrequencies)
    
    #ok now we use itertools to get all the combinations
    kitemsets = [a | b for a, b in itertools.combinations(frequencies.keys(), 2)]

    print(kitemsets)

    for itemset in itemsets:
        for kitemset in kitemsets:
            if kitemset.issubset(itemset):
                if frozenset(kitemset) in frequencies:
                    frequencies[frozenset(kitemset)] += 1
                else:
                    frequencies[frozenset(kitemset)] = 1

    print(frequencies)
    
            
            











    return oldFrequencies

    
# DO NOT CHANGE THE FOLLOWING LINE
def association_rules(itemsets, frequent_itemsets, metric, metric_threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of triples: condition, effect, metric value 
    # Each entry (c,e,m) represents a rule c => e, with the matric value m
    # Rules should only be included if m is greater than the given threshold.    
    # e.g. [(set(condition),set(effect),0.45), ...]
    return []


def main():
    words = ["loquacious", "insidious", "ferocious", "plausible", "atrocious",
                             "thematic", "vindicative", "automated", "pernicious", "advantageous",
                             "ambitious", "suspicious", "contentious", "curious", "guarded", "elusive",
                             "thousand", "approach", "intrusion", "suddenly", "obscure", "island", "ionic",
                             "oust", "obstinate", "foiled", "oily", "spoilers"]
    letters = list(map(set, words))                         
    apriori(letters, .5)

if __name__ == '__main__':
    main()