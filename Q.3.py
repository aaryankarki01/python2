li1=['a','b','c']
li2=[1,2,3]
index=1

for i in range (len(li1)):
    li1.insert(index,li2[i])
    index=index+2

print(li1)
