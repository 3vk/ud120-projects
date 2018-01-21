#!/usr/bin/python

from operator import itemgetter
from operator import attrgetter
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = (net_worths-predictions)** 2
    zipped = zip(ages,net_worths,error)
    zipped.sort(key=itemgetter(2), reverse = True)
    #zipped.sort(key=attrgetter('error'), reverse = True)
    #zipped.sort(key=lambda x: x[2], reverse = True)
    k= int(len(ages)*0.1)
    cleaned_data = zipped[k:]

    
    return cleaned_data

