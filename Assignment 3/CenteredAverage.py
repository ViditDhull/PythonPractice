def centered_average(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    
    sum = 0
    for i in lst:
        sum = sum + i
    return sum/len(lst)  