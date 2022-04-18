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

    #track the number of items?
    totalItems = 0

    #Look at every individual item first

    #for each itemset in the list of itemsets, do this
    for itemset in itemsets:
        #for each item in the itemset, do this
        for item in itemset:
            #increment totalItems so we know how many there are
            totalItems = totalItems + 1
            
            #if this item already exists in frequencies, increment; if not, make it and set it to 1
            if item in frequencies:
                frequencies[item] += 1
            else:
                frequencies[item] = 1


                    
                
    print (frequencies)
    print (totalItems)

    #divide every value inside of frequencies by numberOfItems to get support
    for item in list(frequencies.keys()):
        frequencies[item] = frequencies[item] / totalItems
        #purge anything that has less frequency than our threshold
        if frequencies[item] < threshold:
            oldFrequencies[item] = frequencies.pop(item)

    
    print(frequencies)

    #purge anything that has less frequency than our threshold
    



    #ok now we use itertools to get all the combinations
    itertools.combinations(frequencies.items(), 2)


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
    apriori(letters, .05)

if __name__ == '__main__':
    main()