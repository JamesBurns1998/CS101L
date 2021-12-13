import math

def total(value_list):
    sum = 0
    for i in value_list:
        sum += i
    return float(sum)

def average(value_list):
    avg = (total(value_list)) / len(value_list)
    return avg

def median(value_list):
    value_list.sort()
    length = len(value_list)
    if len(value_list)%2 == 1:
        median = value_list[length//2]
    elif len(value_list)%2 == 0:
        median = (value_list[length//2] + value_list[length//2 - 1]) / 2
    return median

list1 = [1,4,7,9,10,33,22,8]


print(total(list1))
print(average(list1))
print(median(list1))