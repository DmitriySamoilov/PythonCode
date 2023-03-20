#Задача №17.Дан список чисел. Определите, сколько в нем встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6

list =[1, 1, 2, 0, -1, 3, 4, 4]
print(list)
list=sorted(list)
print (list)
i=len(list)-1
count=1
while i>0 :
    if list[i]!=list[i-1] : count +=1
    print(list[i],list[i-1], count)
    i -=1
print (count)
