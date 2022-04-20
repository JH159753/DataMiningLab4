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

    #track the k-itemset size
    #starts at 1 because why would we have empty sets
    ksize = 1

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


    #let's break this down:
    #frequencies is set to itself with the same keys (except for the filtered ones where the frequency is too low for the threshold)
    #and the values assigned to the keys are set to frequency / amount of itemsets we're looking at
    frequencies = {itemset: freq / len(itemsets) for itemset, freq in frequencies.items() if freq / len(itemsets) >= threshold}

    #if frequencies is empty, return oldFrequencies
    if len(frequencies) == 0:
        return oldFrequencies.items()
    #if it is not empty, purge oldFrequencies and then move frequencies' data into it
    else:
        oldFrequencies = frequencies
        frequencies = {}

    while True:
        #ok now we use itertools to get all the combinations
        allCombinationSets = [a | b for a, b in itertools.combinations(oldFrequencies.keys(), 2)]

        #we want to increment ksize now
        ksize += 1

        #make a new list that *only* includes correct size and no duplicates
        kitemsets = list(set([combinationSet for combinationSet in allCombinationSets if len(combinationSet) == ksize]))

        for itemset in itemsets:
            for kitemset in kitemsets:
                if kitemset.issubset(itemset):
                    if frozenset(kitemset) in frequencies:
                        frequencies[frozenset(kitemset)] += 1
                    else:
                        frequencies[frozenset(kitemset)] = 1

        #let's break this down:
        #frequencies is set to itself with the same keys (except for the filtered ones where the frequency is too low for the threshold)
        #and the values assigned to the keys are set to frequency / amount of itemsets we're looking at
        frequencies = {itemset: freq / len(itemsets) for itemset, freq in frequencies.items() if freq / len(itemsets) >= threshold}

        #if frequencies is empty, return oldFrequencies
        if len(frequencies) == 0:
            return oldFrequencies.items()
        #if it is not empty, purge oldFrequencies and then move frequencies' data into it
        else:
            oldFrequencies = frequencies
            frequencies = {}

    

    
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