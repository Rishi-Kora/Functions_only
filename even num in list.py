def eve_num(lst1):
    lst2 = []
    #print(lst1)
    for i in lst1:
        if i%2 == 0:
            lst2.append(i)
    return lst2
           
        
        

print(eve_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
