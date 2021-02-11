try:
    f=open("e:\\name.txt","a")
    print(f)
    #print(f.read())
    #print(f.readline(3333))
    f.write("ab dekho kya hoga Dekho sara likha gaya")

except:
    print("file does not exist")