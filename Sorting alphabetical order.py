def hyp_word(n):
    a = [x for x in n.strip().split("-")]
    print(a)
    #print(type(a))
    a.sort()
    print(a)
    flist = []
    for i in a:
        flist.append(i)
    print(*flist,sep="-")
    

#print(n)

hyp_word("green-red-yellow-black-white")
