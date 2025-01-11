'''
import math
import random


print(math.ceil(2.5))# 2.5 = 3
print(math.floor(2.5))# 2.5 = 2
print(math.pow(2,5))# 2**5 = 32
print(math.sqrt(64))# 64 = 8


print(random.random())# 0......1
print(random.random())# 0......1
print(random.random())# 0......1
print(random.random())# 0......1
print(random.randint(0,1))# 0......1
print(random.randint(0,1))# 0......1
print(random.randint(0,1))# 0......1
print(random.randint(1,100))#1......100
print(random.randint(10,20))#10......20


# Уявіть, що ви прийшли в магазин, де продають магічні 
# карамельки по 270 монет за 1 кг. Зараз
# у магазині проходить акція: при покупці більше, 
# ніж 500 г карамелек, їхня вартість дорівнює 200 монетам за 1 кг..

full_price = 270
sale_price = 200
gramm = int(input("Enter weight (gramm) : "))# 700 g
kg = gramm/1000# 0.7 kg
print(f"Your candies  weight : {kg} kg")
if kg < 0.5:
    total = kg * full_price
else:
    total = kg * sale_price

print(f"Your total price  : {total} coins ")
'''
# #Ctrl + K + C - comment
# #Ctrl + K + U - uncomment

# day = int(input("Enter number of day [1-7] : "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")   
# elif day == 7:
#     print("Sunday")
# else:
#     print("Error number day ")

# #match
# print(" [1] - add numbers [2] = minus [3] - average [4] - dobutok")
# key = int(input("Enter your choice : "))


# day = int(input("Enter number of day [1-7] : "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")   
#     case 7:
#         print("Sunday")
#     case _:
#         print("Error number day ")

number=  int(input("Enter number  [100 - 999] : "))
#123
a = number//100 #123//100= 1
b= number//10%10#123//10 = 12%10 = 2
c = number%10
print(a,b,c)

# 10/2 = 5.0
# 10%2 = 0
# 11%2 = 1
# number %2 == 0 #parne
# number %2 == 1 # ne parne
# number %7 == 0 # kratne 7