f=open("C:\\Users\\Public\\Pictures\\Sample Pictures\koala.jpg","rb")
#print(f.read())
f1=open("meraphoto.jpg","wb")
for data in f:
    print(data)
    f1.write(data)