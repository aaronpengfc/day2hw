math = input("math score")
math = int(math)
eng = input("eng score")
eng = int(eng)
if math >90 and eng >90:
    print("prize")
elif math <60 and eng <60:
    print("fail")
elif math <60 or eng <60:
    print("go go")


