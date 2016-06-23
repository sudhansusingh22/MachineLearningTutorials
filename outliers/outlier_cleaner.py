#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    errors = []
    for p,n in zip(predictions, net_worths):
        errors.append((p-n)[0])
    errors.sort()
    x = int(len(errors)*.1)
    errors = errors[:len(errors)-x]
    for a,n,p in zip(ages,net_worths,predictions):
        if((p-n)[0] in errors):
            cleaned_data.append([a,n,p-n])

#     print(cleaned_data)
    ### your code goes here

    
    return cleaned_data

