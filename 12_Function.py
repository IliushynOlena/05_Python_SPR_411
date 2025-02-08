

# # print()
# # print("Hello")
# # print("Hello",5)
# # print("Hello",5,True)
# # print(5)

# # input()
# # sum()
# # max()
# # min()

# # help(min)
# # help(print)

# def showHello():
#     print("Hello")


# showHello()
# showHello()
# showHello()
# showHello()
# showHello()
# showHello()


# a = 100#gloabal
# print(f"a = {a}")

# def sayHello(name):
#     print(f"Hello, {name}")
#     # summa = 0 local variable
#     # #sum(list) = summa = 1500
#     # print(summa)

#     # print(f"a = {a}")


# sayHello("Olena")
# sayHello("Ivan")
# sayHello("Kateruna")
# sayHello("Nazar")
# # name = input("Enter name : ")
# # sayHello(name)


# # def summa(a,b):
# #     print(a + b )

# # def summa(a,b):
# #     res = a + b 
# #     print(res)

# # def summa(a,b):
# #     res = a + b 
# #     return res

# # print (summa(2,5))
# # sum = summa(10,5)
# # print(f"Summa = {sum}")
# # sum = summa(3,7)
# # print(f"Summa = {sum}") 

# def summa(a,b):
#     return a + b 

# def sub(a,b):
#     return a - b 

# def multy(a,b):
#     return a * b 

# def div(a,b):
#     if b == 0:
#         return #return == break
#     return a / b 

# def calculator(a,b,op):
#     if op == '+':
#         return summa(a,b)
#     if op == '-':
#         return sub(a,b)
#     if op == '*':
#         return multy(a,b)
#     if op == '/':
#         return div(a,b)


# # res = calculator(10,7,'+')
# # print(f"Res = {res}")
# # res = calculator(10,7,'-')
# # print(f"Res = {res}")
# # res = calculator(10,7,'*')
# # print(f"Res = {res}")
# # res = calculator(10,7,'/')
# # print(f"Res = {res}")

# def getOperation(example):
#     if example.find('+') != -1:
#         return '+'
#     if example.find('-') != -1:
#         return '-'
#     if example.find('*') != -1:
#         return '*'
#     if example.find('/') != -1:
#         return '/'

# example = input("Enter example (2 + 2 )")# 25 * 24
# op = getOperation(example)
# num1 = float(example.split(op)[0])
# num2 = float(example.split(op)[1])
# res = calculator(num1,num2,op)
# print(f"Res = {res}")
import random
#count = 15, min = 20, max = 50 - default value
def fillList( count = 15, min = 20, max = 50):
    return [ random.randint(min, max) for i in range(count)]



numbers = []
print(numbers)
numbers = fillList(10,1,20)
print(numbers)
numbers = fillList()
print(numbers)
numbers = fillList(40)
print(numbers)
numbers = fillList(5,1)
print(numbers)
numbers = fillList(7,100,200)
print(numbers)