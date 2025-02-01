'''
line = "Hello"
print(line)
print(id(line))
line = "admin"
print(line)
print(id(line))
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])


#list
#1
category = ["Drama","Comedy","Fantasy"]
print(category)
#2
courses = list(("Python","C++","C#","SQL"))
print(courses)

studentMarks= []
students = list()
print(studentMarks)
print(students)

my_list = ["Hello",2563,14,5.8,78.3,"Database",True,False,[1,2,5,8,9]]
print(my_list)
print(my_list[0])
print(my_list[5])
print(my_list[7])
print(my_list[8])
print(my_list[8][0])

customers = ['Bob',"Jack","Tom",'Anna','Bob',"Jack","Tom"]
print(customers)

myLetter = list("qwerrtyuio")
print(myLetter)

#створення списку з використанням генераторів
#newList = [expession for item in sequence]
#expession - вираз або формула для одного елементу
#for item in sequence - цикл, який дає нам послідовність елементів(або кількість ітерацій)

#for i in range(6) ---> 0 1 2 3 4 5
# for i in range(6):
#     print(i)
list_1 = [i  for i in range(6)]
print(list_1)

list_2 = [i*i  for i in range(6)]
print(list_2)

list_3 = [i+10  for i in range(6)]
print(list_3)

import random
numbers = [random.randint(20,50)  for i in range(10)]
print(numbers)

#виводимо всі елементи списку за допомогою циклу
for num in numbers:
    print(num,end= " ")
print()

#for i in "example" -----> e x a m p l e
list_4 = [ i+"*"   for i in "example"]
print(list_4)

line = [l for l in "language"]
print(line)

newLine = "_".join(line)
print(newLine)

newLine = "".join(line)
print(newLine)

colors = "red white grey green pink blue yellow magenta lime"
list_colors = colors.split(' ')
print(list_colors)

list_5 = [ i*5  for i in "abcdefg"]
print(list_5)

#при генерації елементів списку можна вказати умову, які саме елементи брати з послідовності
#пif condition  - умова
#newList = [expession for item in sequence if condition ]
list_6 = [i for i in range(1,11) if i%2==0]
print(list_6)

list_6 = [i for i in range(1,11) if i%2!=0]
print(list_6)

customers = ['Bob',"Jack","Tom",'Anna','Bob',"Jack","Tom"]
print(customers)

list_7 = [ c for c in customers if c != "Bob" and c != "Jack"]
print(list_7)

# for x in range(1,4):
#     for y in range(1,4):
#         print(x*y, end=" ")
#     print()

list_8 = [x*y  for x in range(1,4) for y in range(1,4)]
print(list_8)

myList = ["Math",2365,5.13,"Yellow",True, False,[1,45,23,14]]
print(myList)
print(myList[0])
print(myList[2])
print(myList[len(myList)-1])
print(myList[-1])
#зріз = [start : stop : step]
print(myList[1:3])
print(myList[-4:-2])
print(myList[1:-1])
# #reverse 
print(myList[::-1])
print(myList[4::-1])
print(myList[-4::-1])

category =["Drama", "Comedy", "Fantasy"] 
print(category)
print(category[0])
category[0]= "Action"
print(category[0])
print(category)


userLogs = ["admin","student","teacher","hr","user"]
prices = [100,200,30,400,50]
print(len(userLogs))
print(len(prices))

print(sorted(userLogs))
print(sorted(prices))

print(min(userLogs))
print(min(prices))

print(max(userLogs))
print(max(prices))

#print(sum(userLogs)) #error
print(sum(prices))

#operator + 
category1 = ["Drama", "Comedy", "Fantasy","History"]
category2 = ["Cartoon","Horor","History","Science"]
print(category1+ category2)
print(category1*2)

for film in category1:    
    print(film)

print(category1)
# range(len(category1)) --> staert = 0, end = 4-1, step = 1 
# index ---> 0 1 2 3 
for index in range(len(category1)):#0 1 2 3
    #category1[index] = "Error"
    print(category1[index])

print(category1)
'''

print("Methods list : ")
category = ["Drama", "Comedy", "Fantasy","History"]
category2 = ["Cartoon","Horor","History","Science"]
print(category)
#add to the end one element
category.append("Cartoon")
print(category)
#add to the end list of elements
category.extend(["Cartoon","Horor","History","Science"])
#category.extend(category2)
print(category)
# add element in the index
category.insert(1,"History")
print(category)

#delete element by value
category.remove("Drama")
print(category)
#delete element by index
category.pop(0)
print(category)
#delete last element
category.pop()
print(category)
# #delete all elements
# category.clear()
# print(category)

#find element by value 
print("Find element History in index - " ,category.index("History"))
#print("Find element History in index - " ,category.index("Historyyyyyyy")) - nor found

count_h = category.count("History")
print(f"Count History element = {count_h}")

print(sorted(category))#return copy of sorted list
print(category)

category.sort()
print(category)

category.sort(reverse=False)
print(category)


category.sort(reverse=True)
print(category)

customers = ['Bob',"Jack","Tom",'Anna','Bob',"Jack","Tom"]

for c in customers:
    if c == "Anna":
        print("Anna is in the collection")

if "Anna" in customers:
    print("Anna is in the collection")
else:
    print("Error")

numbers = [1,2,3,4,5,6]

#copy_numbers = numbers --? error
#copy 
#1 use method copy
#copy_numbers = numbers.copy()
#2 - use constructor list()
#copy_numbers = list(numbers)
#3- use [:]
copy_numbers = numbers[:]
print(f"Numbers = {numbers}")
print(f"Copy Numbers = {copy_numbers}")

copy_numbers[0]= 1000
print(f"Numbers = {numbers}")
print(f"Copy Numbers = {copy_numbers}")
