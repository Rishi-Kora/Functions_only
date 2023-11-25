def mysum(lst1):
    total = 0.0
    for i in lst1:
        try:
            total += float(i)
        except(ValueError, TypeError):
            return 0.0
    return total    
