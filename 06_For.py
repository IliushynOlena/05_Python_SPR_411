
line = "Hello, world"
print(line)
print(line[0])
print(line[1])
print(line[2])
print(line[3])

# start = 0 --- Start
# end = 12 --- end = 12
# while start <= end:
#     print(start, end=" ")
#     start+=1 ---> step = 1

#[start = 0, end = 12, step = 1]
for letter in line:
    print(letter, end=" ")

print("Continue .....")
#[start , end, step ]
for letter in line[0:5]:
    print(letter, end=" ")
print()
for letter in line[0:13]:
    print(letter, end=" ")

print()
for letter in line[7:13]:
    print(letter, end=" ")

print()
for letter in line[:]:
    print(letter, end=" ")

print()
for letter in line[::2]:
    print(letter, end=" ")
print()

for letter in line[0:10:2]:
    print(letter, end=" ")
print()
# start = 0, end = 10-1, step = 1
for number in range(10):
    print(number, end= " ")
print()

# start = 10, end = 20-1, step = 1
for number in range(10, 20):
    print(number, end= " ")
print()


# start = 10, end = 20-1, step = 2
for number in range(10, 20, 2):
    print(number, end= " ")
print()

#вивести всі числа від 5 до 20
# start = int(input("Enter start : "))
# end = int(input("Enter end : "))
# for num in range(start, end + 1):
#     print(num, end=" ")
# while True:
#     res = int(input(" 2 + 2 = ???  ---> "))
#     if res == 4:
#         print("Congatulation!!!!!! ")
#         break
#     else:
#         print("Error res ")

# i = 0
# end = int(input("Enter end : "))
# while i <= end :
#     i +=1
#     # if i%3 != 0:
#     #     print(i, end=" ")
#     if i%3 == 0:
#         continue
#     print(i, end=" ")

# # start = 10, end = 20-1, step = 1
# sum = 0# 0 + 10 +11 +12 +13 +14 +15..20
# count = 0
# for number in range(10, 20):
#     sum += number
#     count += 1
#     if number%4 ==0:
#         print(number, end= " ")
# print()
# counter_div = 0
# number = int(input("Enter number : "))
# #8 ---> 8/1 8/2 8/3 8/4 8/5 8/6 8/7 8/8  
# #4 ---> 4/1 4/2 4/3 4/4
# for i in range(1, number+1):
#     if number%i == 0:
#         counter_div+=1
# print(f"Count divisions {counter_div}")
# if counter_div > 2:
#     print("Number is compound")
# else :
#     print("Number is  prime")

flag = True
number = int(input("Enter number : "))
#100 100/1 100/2 100/50 100/51
for i in range(2, number//2+1):
    if number%i == 0:
        flag = False
        break
#flag = True    or flag = False
#True --> not True = False 
#False --> not False = True
if not flag :
    print("Number is compound")
else :
    print("Number is  prime")

if flag:
    print("Number is  prime")
else:
    print("Number is compound")