li1=[3,5,4,8,7,9]
for i in range (len(li1)):
    for j in range(len(li1)-1):
        if li1[j]>li1[j+1]:
            li1[j],li1[j+1]=li1[j+1],li1[j]
print(li1)