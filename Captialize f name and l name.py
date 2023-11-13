def cap_name(fname,lname):
    x = fname.upper()
    y = lname.upper()
    return x,y


print(*cap_name("Rishi","Kora"))

print(type(cap_name))
