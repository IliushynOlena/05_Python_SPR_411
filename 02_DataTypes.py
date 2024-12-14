
print("2")
print(2)

#Data types
# number ==> int (integer), float
# str - symbols
# boolean (bool) logic type

print("int ", type(2))
print("str ", type("2"))
print("float ", type(3.14))
print("bool ", type(True))
print("bool ", type(False))
# + - 
print(2 + 2)

print(7-5)
# *
print(4 * 9.)
print(4 * 9)
print(4. * 9)
print(4. * 9.)
# /
print(18 / 3)
print(18 / 3.)
print(18. / 3)
print(18. / 3.)
#operator + , - , * , /, //, %, **
# **
print(2 ** 3)
print(2 ** 3.0)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
# //
print(6/3)#2.0
print(6/4)#1.5

print(6//3)#2
print(6//4)#1

# % 
print(12%4) # 12/4 = 3.0   4*3 = 12  12-12 = 0
print(17%4) # 17/4 = 4.25   4*4 = 16  17 - 16 = 1

print(8/2)
print(9/2)
print(8%2)
print(9%2)
#Error
#print(9/0)
#print(9//0)
#print(9%0)

print(-5 + 7)
print( 2 + 3 * 5 )# <------------------
print( (2 + 3) * 5 )# ---------------------->
print( 2 * 5 * 7) #------------------>
print(2 ** 2 ** 3)# <------------------- 64


print(5 + 2.5)  # = 7.5
#print(5 + "str")# = error
print(5 + True) # = 5  True = 1
print(5 + False)# ????? False = 0

print(1_000_000)

a = 10
pi = 3.14
age = 25
name = "Olena"
Age = 45
age1 = 54
#1age= 12
a_1 = 1
a_2 = 2
AgeOfMan = 47
age_of_man = 41
# print(age)
# print = 5
# print(age)

var = 1
print(1)
print(var)

square = 0
print(square)

first_number = 10
second_number = 25
#first_number = 3.14
#print(10 + 25)
print(first_number + second_number)
result = first_number + second_number
print("Result =", result)
print("first_number =", first_number)
print("second_number =", second_number)
#first_number = first_number + 5
first_number += 5
print("first_number =", first_number)
first_number -= 5
print("first_number =", first_number)
first_number *= 5
print("first_number =", first_number)
first_number /= 5
print("first_number =", first_number)


line_1 = "Hyper"
line_2 = "Text"
line_3 = "Markup"
line_4 = "Language"
allLine = line_1 + " " + line_2+ " " + line_3+ " " + line_4
print(allLine)
print("="*40)
print(allLine*3)

print("\033[31m\033[45m\033[1m",line_1, "\033[0m", end=" ")
print("\033[32m\033[44m\033[2m",line_2, "\033[0m", end=" ")
print("\033[33m\033[46m\033[3m",line_3,"\033[0m", end=" ")
print("\033[34m\033[47m\033[4m",line_4, "\033[0m",end=" ")
print("\033[0m")
print(allLine)
print("="*40)
print(allLine*3)



first_number = int(input("Enter first number : ")) 
second_number = float(input("Enter second number : ")) 

result = first_number + second_number
print("Result =", result)
