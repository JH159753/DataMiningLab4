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
            if frozenset({item}) in frequencies:
                frequencies[frozenset({item})] += 1
            else:
                frequencies[frozenset({item})] = 1


    #let's break this down:
    #frequencies is set to itself with the same keys (except for the filtered ones where the frequency is too low for the threshold)
    #and the values assigned to the keys are set to frequency / amount of itemsets we're looking at
    frequencies = {itemset: freq / len(itemsets) for itemset, freq in frequencies.items() if freq / len(itemsets) > threshold}


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
        frequencies = {itemset: freq / len(itemsets) for itemset, freq in frequencies.items() if freq / len(itemsets) > threshold}

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

    possibleRules = []
    metricValue = 0
    
    
    for itemset, frequency in frequent_itemsets:
        #frequency is support(T)

        #set currentPowerset to hold the stuff we are looking at right now
        currentPowerset = list(powerset(itemset))

        #for every antecedent in currentPowerset, do this
        for antecedent in currentPowerset:

            #probably calculate the consequence here, then after you have that, calculate the metric value based on the given metric
            consequence = itemset.difference(antecedent)
            
            metricValue = calculateMetricValue(antecedent, consequence, frequency, itemsets, metric)

            possibleRules.append([set(antecedent), consequence, metricValue])


    #after getting all the possible rules, use list comprehension to clip anything below our given metric_threshold

    actualRules = [possibleRule for possibleRule in possibleRules if possibleRule[2] > metric_threshold]

    return actualRules

def calculateMetricValue(antecedent, consequence, frequency, itemsets, metric):
    #frequency is support(T)
    if metric == "lift":
        #need P(B|A) and P(B) aka P(consequence|antecedent) and P(consequence)

        #this is P(consequence) part
        probB = 0
        #for each itemset, check if the consequence is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            if consequence.issubset(itemset):
                probB += 1
        #at the end, divide by len(itemsets)
        probB = probB / len(itemsets)

        #this is P(antecedent) part
        probA = 0
        #for each itemset, check if the antecedent is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            #this is a bit spaghetti but since antecedent is a tuple and not a set, we need to do set() on it to use the .issubset function
            if set(antecedent).issubset(itemset):
                probA += 1
        #at the end, divide by len(itemsets)
        probA = probA / len(itemsets)

        #make sure we don't run into dividing by 0 issues
        if (probA == 0 or probB == 0):
            return 0
        #this is P(consequence|antecedent) because support(T) / support(A) is that, divided by prob(B)
        return((frequency / probA) / probB)

        
    elif metric == "all":
        #need P(B|A) and P(B) aka P(consequence|antecedent) and P(consequence)

        #this is P(consequence) part
        probB = 0
        #for each itemset, check if the consequence is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            if consequence.issubset(itemset):
                probB += 1
        #at the end, divide by len(itemsets)
        probB = probB / len(itemsets)

        #this is P(antecedent) part
        probA = 0
        #for each itemset, check if the antecedent is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            #this is a bit spaghetti but since antecedent is a tuple and not a set, we need to do set() on it to use the .issubset function
            if set(antecedent).issubset(itemset):
                probA += 1
        #at the end, divide by len(itemsets)
        probA = probA / len(itemsets)

        #make sure we don't run into dividing by 0 issues
        if (probA == 0 or probB == 0):
            return 0

        #with P(B) and P(A) and P(T) calculate P(A|B) and P(B|A)
        return min((frequency / probA), (frequency / probB))

        
    elif metric == "max":
        #need P(B|A) and P(B) aka P(consequence|antecedent) and P(consequence)

        #this is P(consequence) part
        probB = 0
        #for each itemset, check if the consequence is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            if consequence.issubset(itemset):
                probB += 1
        #at the end, divide by len(itemsets)
        probB = probB / len(itemsets)

        #this is P(antecedent) part
        probA = 0
        #for each itemset, check if the antecedent is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            #this is a bit spaghetti but since antecedent is a tuple and not a set, we need to do set() on it to use the .issubset function
            if set(antecedent).issubset(itemset):
                probA += 1
        #at the end, divide by len(itemsets)
        probA = probA / len(itemsets)

        #make sure we don't run into dividing by 0 issues
        if (probA == 0 or probB == 0):
            return 0

        #with P(B) and P(A) and P(T) calculate P(A|B) and P(B|A)
        return max((frequency / probA), (frequency / probB))

    elif metric == "kulczynski":
        #need P(B|A) and P(B) aka P(consequence|antecedent) and P(consequence)

        #this is P(consequence) part
        probB = 0
        #for each itemset, check if the consequence is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            if consequence.issubset(itemset):
                probB += 1
        #at the end, divide by len(itemsets)
        probB = probB / len(itemsets)

        #this is P(antecedent) part
        probA = 0
        #for each itemset, check if the antecedent is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            #this is a bit spaghetti but since antecedent is a tuple and not a set, we need to do set() on it to use the .issubset function
            if set(antecedent).issubset(itemset):
                probA += 1
        #at the end, divide by len(itemsets)
        probA = probA / len(itemsets)

        #make sure we don't run into dividing by 0 issues
        if (probA == 0 or probB == 0):
            return 0

        #with P(B) and P(A) and P(T) calculate P(A|B) and P(B|A)
        return ((frequency / probA)+(frequency / probB))/2
    elif metric == "cosine":
        #need P(B|A) and P(B) aka P(consequence|antecedent) and P(consequence)

        #this is P(consequence) part
        probB = 0
        #for each itemset, check if the consequence is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            if consequence.issubset(itemset):
                probB += 1
        #at the end, divide by len(itemsets)
        probB = probB / len(itemsets)

        #this is P(antecedent) part
        probA = 0
        #for each itemset, check if the antecedent is a subset, if it is, increment, if not, do nothing
        for itemset in itemsets:
            #this is a bit spaghetti but since antecedent is a tuple and not a set, we need to do set() on it to use the .issubset function
            if set(antecedent).issubset(itemset):
                probA += 1
        #at the end, divide by len(itemsets)
        probA = probA / len(itemsets)

        #make sure we don't run into dividing by 0 issues
        if (probA == 0 or probB == 0):
            return 0

        #with P(B) and P(A) and P(T) calculate P(A|B) and P(B|A)
        return ((frequency / probA)*(frequency / probB))**(.5)


    else:
        print ("This is not a valid metric")

    


#steal powerset code from https://docs.python.org/3/library/itertools.html#itertools-recipes
#slightly modified to not include empty set and full set
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, len(s)))


def to_set(row):
    result = set(row[1].split(";"))
    return result

def main():
    words = ["loquacious", "insidious", "ferocious", "plausible", "atrocious",
                             "thematic", "vindicative", "automated", "pernicious", "advantageous",
                             "ambitious", "suspicious", "contentious", "curious", "guarded", "elusive",
                             "thousand", "approach", "intrusion", "suddenly", "obscure", "island", "ionic",
                             "oust", "obstinate", "foiled", "oily", "spoilers"]
    #letters = list(map(set, words))                         
    #apriori(letters, .3)
    #print(association_rules(letters, apriori(letters, .3), "lift", .71))


    df = pd.read_csv("recipes.csv")
    data = [to_set(item) for (idx,item) in df.iterrows()]
    
    print(data)
    print(apriori(data, 0.005))
    print(association_rules(data, apriori(data, .005), "max", .05))
    
        

if __name__ == '__main__':
    main()