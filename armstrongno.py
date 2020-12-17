num=int(input("enter three digit number"))
sum=0
org=num
while num>0:
        a=num%10
        sum=sum+a*a*a
        num=num//10
if org==sum:
    print("Arm strong")
else:
    print("not arm strong")
print("sum=",sum)



