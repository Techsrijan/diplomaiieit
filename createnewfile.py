try:
    f=open("e:\\name.txt","r")
    f1 = open("e:\\name2.txt", "w")
    #print(f)
    for data in f:
        print(data)
        f1.write(data)

except:
    print("file does not exist")