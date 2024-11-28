from itertools import count

values = [100,21,100,35,48,100,100,66]
print(values)

#add an element at the end of the list
values.append(100)
print(values)

#add an element in a given position of the list
values.insert(1,0.5)
print(values)

#remove an element from the list using the index
values.pop(2)
print(values)

#remove an element from the list using its value
values.remove(100)                  #remove only works once
print(values)

#remove an element using its value counting from the end of the list
values.reverse()
values.remove(100)
values.reverse()
print(values)

#sort the list
values.sort()
print(values)

#count the number of occurence
count = values.count(100)
print(count)

#extend a list by adding new values
values.extend([11,18,20])
print(values)

#find the index of the first given value
index_of_100 = values.index(100)        #index only shows the first one
print(index_of_100)