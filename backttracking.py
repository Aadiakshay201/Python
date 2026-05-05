def akshay(a):
    if a==1:
        return
    a -=1
    akshay(a)
    print("hello ", end="")
    akshay(a)
akshay(5)
