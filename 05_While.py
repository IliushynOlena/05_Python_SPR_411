

'''

i = 0
while i < 10:
    i +=1
    print(i , "Hello world")

#вивести всі числа від 5 до 20
#1. create iterator
i = 5
#2 create while 
while i <= 20: #5 6 7 8 9 .....20
    print(i, end=" ")
    # add iterator
    i+=1

print("Continue.......")

#вивести всі числа від 10 до 0
i = 10
while i > 0: #10 98 7 6 5 4 3 2 1 0
    print(i, end=" ")
    i -=1

print("Continue.......")

i = int(input("Enter number ---> ")) 
if i <= 20:
    while i <= 20: # i = 5 5 6 7 8 9 ...20
        print(i, end=" ")
        i+=1
else:
    while i >= 20:# i = 30 30 29 28 27 26 25 24 23 22 21 20
        print(i, end=" ")
        i-=1

#користувач вводить число…вивести таблицю множення на це число
number = int(input("\nEnter number ---> ")) 

if number< 0 or number > 10:
    print("Error number.....")
else:
    i = 1
    while i <= 10:
        print(f" {number} * {i} = {number*i}")
        i+=1
    else:
        print("="*30)
#10/2 = 5.0
#11/2 = 5.5
#number%2 == 0 - parne
#number%2 != 0 - ne parne
'''
start = int(input("\nEnter start number ---> ")) #1
end = int(input("\nEnter end number ---> ")) # 10
i = start
while i <= end:
    if i%2 != 0:
        print(i, end=" ")
    i +=1 


