li = [[24, 3, 6], [8, 12, 18], [2, 66, 7]]
min_value = li[0][0]
max_value = li[0][0]

for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j] % 2 == 0 and li[i][j] % 3 == 0:
            print(f"{li[i][j]} is divisible by both 2 and 3")
        
    
        if li[i][j] > max_value:
            max_value = li[i][j]
        
    
        if li[i][j] < min_value:
            min_value = li[i][j]

print("The maximum value in the 2D list is:", max_value)
print("The minimum value in the 2D list is:", min_value)
