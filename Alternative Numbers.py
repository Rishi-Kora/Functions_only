#9. Create new list with alternating values from this list lst=[23,32,24,34,26,39]
def alter_num():
    lst = [23,32,24,34,26,39]
    new_lst = []
    for i in range(0,len(lst),2):
        #print(lst[i])
        new_lst.append(lst[i])
    print(new_lst)        




alter_num()
