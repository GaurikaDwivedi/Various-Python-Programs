name = input("enter name to be reversed with spaces: ")

name = name.split(',')

for name in name:
    leng = len(name) 

print (leng)
for x in name:
    print(name[leng-1])
    leng-=1
    
   
