
my_list=[4,5,6,8,9,4,3,5,7,52,4,6,7,8,2,21,13,4,56,7,7]
my_list=sorted(my_list)
unique=[my_list[0]]

for i in range(1,len(my_list)):
    if my_list [i] !=my_list[i-1]:
        unique.append(my_list[i])

print(unique)