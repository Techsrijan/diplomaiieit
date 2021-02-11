num=int(input("how many toffe u want"))
av=10
i=1
while i<=num:
    if i<=av:
        print("Plese collect toffee=",i)
    else:
        print("out of stock")
        break
    i=i+1
else: # this else will run when loop properly runs
    print("Thanks Please Visit again")