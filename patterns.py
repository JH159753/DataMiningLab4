import math
import csv
import pandas as pd
import numpy as np



# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE

    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]
    
    #first I guess we figure out how to pull all sets?

    #declare a set to store what we want to return (a list of sets, each set has frequent itemset and support)
    listOfSets = []

    #track the number of items?
    numberOfItems = 0

    #track if the item has found a match?
    validMatch = 0

    #Look at every individual item first
    for set in itemsets:
        for item in set:
            numberOfItems = numberOfItems + 1
            #if the item is not in listOfSets, then add it, if the item is in the list, keep track of it
            for things in listOfSets:
                #if the item matches, add 1 to its count
                if item == things[0]:
                    things[1] = things[1] + 1
                    validMatch = 1
            #if the item does not match at the end
            if validMatch == 0:
                #append with item, 1 because this is the first instance of that item
                listOfSets.append([item, 1])
                    
                
    print (listOfSets)
    print (numberOfItems)
    #divide every value inside of listOfSets by numberOfItems to get support
    for things in listOfSets: 
        things[1] = things[1] / numberOfItems
    
    print(listOfSets)

    



    return listOfSets

    
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
    apriori(letters, 0)

if __name__ == '__main__':
    main()