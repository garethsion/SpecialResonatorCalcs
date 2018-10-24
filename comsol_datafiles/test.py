file = 'Bx.txt'
f=open(file,"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split(' ')[1])
f.close()
print(result)
