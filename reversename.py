name = input("enter name to be reversed with spaces: ")

name = name.split(',')

for name in name:
    leng = len(name) 

print (leng)
for x in name:
    print(name[0][leng])
    leng-=1
    
   
