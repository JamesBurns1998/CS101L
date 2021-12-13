import math

def total(value_list):
    '''iterates through values in value_list to return sum of values in list'''
    sum = 0
    for i in value_list:
        sum += i
    return float(sum)

def average(value_list):
    '''calls total(value_list) to find average value in list by dividing sum by length of list'''
    try:
        avg = (total(value_list)) / len(value_list)
        return avg
    except ZeroDivisionError:
        return math.nan

def median(value_list):
    value_list.sort()
    length = len(value_list)
    if length == 0:
        raise ValueError
    elif len(value_list)%2 == 1:
        median = value_list[length//2]
        return median
    elif len(value_list)%2 == 0:
        median = (value_list[length//2] + value_list[length//2 - 1]) / 2
        return median
    
    
