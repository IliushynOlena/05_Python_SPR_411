# def summa(a,b):
#     return a + b 


# print(summa(5,6))
# #print(summa(5))
# #print(summa(5,5,8))

# print()
# print(5)
# print(5,6)
# print(5,6,7)
# print(5,6,7,956,547)

# def summaAllElements(*args):
#     temp = list(args)
#     print(temp)
#     #args[0] = 55#error
#     print(args)

#     for elem in args:
#         print(elem, end= " ")

#     print()
#     print(f"Element in index [0] {args[0]}")
#     print(f"Fing Element  [8] at index - {args.index(8)}")
#     print(f"Count Element  [1] - {args.count(1)}")
#     print(f"Lenght   - {len(args)}")
#     return sum(args)


# sum = summaAllElements(5,7,8,9,6,3,1,1,1,1,2,4)
# print(f"Summa = {sum}")


# def fullInfo(name, age, *marks):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"Marks : {marks}")

# fullInfo("Mukola",18,12,10,11,4,12,10,9)

#lambda functions 
def summa(a,b):
    return a + b 

def show(color):
    print(color)

print(summa(5,8))
show("red")

lambda_sum = lambda a,b:a+b
lambda_show = lambda color:print(color)
print(lambda_sum(10,5))
lambda_show("green")

#1.1
def modifyList(numbers):
    new_list = []
    for el in numbers:
        new_list.append(el*2)
    return new_list


numbers = [10,5,7,89,6,2,4,712,45,6]
new_numbers = modifyList(numbers)
print(numbers)
print(new_numbers)
print("-------------------------------------------------")
#1.2
# def double(x):
#     return x*2
#map() - function change one by one all element in collection
numbers = [10,5,7,89,6,2,4,712,45,6]
#new_numbers_2 = list(map(double,numbers))
#new_numbers_2 = list(map(lambda x:x*2,numbers))
#new_numbers_2 = list(map(lambda x:x*x,numbers))
new_numbers_2 = list(map(lambda x:x+x,numbers))
print(numbers)
print(new_numbers_2)

# #2.1
# line = input("Enter all numbers : ").split(' ')#5 8 9 6 7 4 2 3 
# line = [int(item)  for item in line]
# print(line)
#2.2
# line =list( map(int,input("Enter all numbers : ").split(' ')))#5 8 9 6 7 4 2 3 
# print(line)


#filter()
numbers = [10,5,7,89,6,2,4,7,1,2,4,5,6]

# def parne(x):
#     if x%2==0:
#         return True
#     else:
#         return False
even = list(filter(lambda x:x%2==0, numbers))
print(numbers)
print(even)
odd = list(filter(lambda x:x%2!=0, numbers))
print(odd)

new_list = list(filter(lambda x:x > 0 and x < 10, numbers))
print(new_list)


colors = ["red","green","blue","yellow","black","white","purple"]

# def checkColor(color):
#     if len(color)> 4:
#         return True
#     else:
#         return False
# def checkColor(color):
#     return len(color)> 4
    
print(colors)
#new_colors = list(filter(checkColor, colors))
new_colors = list(filter(lambda color:len(color)>4, colors))
print(new_colors)
#123420%10 = 0
#12342/10%10 = 0