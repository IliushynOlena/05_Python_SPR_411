import re

#operator . ^ $ * + ? [] {} () \ |
#    СПЕЦ. СИМВОЛИ
#     \d - Визначає символи цифр. 
#     \D - Визначає любий символ, який не є цифрою. 
#     \w - Визначає любий символ цифри, букви або нижнє підкреслення. 
#     \W - Визначає любий символ, який не є цифрою, буквою або нижнім підкресленням.. 
#     \s - Визначає любий недрукований символ, включаючи пробіл. (таб і перехід на новий рядок)
#     \S - Визначає любий символ, крім символів табуляции, нового рядка и повернення каретки.
#     .  - Визначає любий символ крім символа нового рядка.  
#     \. - Визначає символ крапки.

#   КВАНТИФИКАТОРЫ
#     ^ - з початку рядка. 
#     $ - з кінця рядка. 
#     * - нуль і більше входжень підшаблону в сторці.  
#     + - одне і більше  входжень підшаблону в сторці.  
#     ? - нуль чи одне  входження підшаблону в сторці.    

str_1 = "123"
str_2 = "234"
str_3 = "Lorem 21 ipsum red"

print(f"\t{str_1} ---> {re.search('1',str_1)}")
print(f"\t{str_2} ---> {re.search('1',str_2)}")
print(f"\t{str_3} ---> {re.search('1',str_3)}")

print(f"\t{str_1} ---> {re.search('12',str_1)}")
print(f"\t{str_2} ---> {re.search('12',str_2)}")
print(f"\t{str_3} ---> {re.search('12',str_3)}")

print(f"\t{str_1} ---> {re.search('[0-9]',str_1)}")
print(f"\t{str_2} ---> {re.search('[0-9]',str_2)}")
print(f"\t{str_3} ---> {re.search('[0-9]',str_3)}")

print(f"\t{str_1} ---> {re.search('[a-z]',str_1)}")
print(f"\t{str_2} ---> {re.search('[a-z]',str_2)}")
print(f"\t{str_3} ---> {re.search('[a-z]',str_3)}")
# while True:
#     letter = input("Enter symbol ----> ")
#     match = re.search("[a-zA-Z]", letter)
#     if match:
#         print("This is letter")
#     else:
#         print("This is not letter")
print(f"\t{str_1} ---> {re.search('[a-zA-Z]{5}',str_1)}")
print(f"\t{str_2} ---> {re.search('[a-zA-Z]{5}',str_2)}")
print(f"\t{str_3} ---> {re.search('[a-zA-Z]{5}',str_3)}")
print(f"\t{str_3} ---> {re.search('[a-zA-Z]{6}',str_3)}")

print(f"\t{str_1} ---> {re.search('[a-zA-Z]+',str_1)}")
print(f"\t{str_2} ---> {re.search('[a-zA-Z]+',str_2)}")
print(f"\t{str_3} ---> {re.search('[a-zA-Z]+',str_3)}")

print(f"\t{str_3} ---> {re.search('Lorem',str_3).group()}")
print(f"\t{str_3} ---> {re.search('Lorem',str_3).group(0)}")

words = re.findall("\w+",str_3)
print(words)
for word in words :
    print(word)

#шукає всі співпадіння в тексті з заданим шаблоном і дозволяє йоно змінити на нове
print('=========================== re.findall(pattern, str)=====================')
#print(f"\t{str_3} ----> \t {re.sub('\w+', "white",str_3)}")
print(f"\t{str_3} ----> \t {re.sub('\w{3}', "white",str_3)}")


# pattern = "^\+38\d{10}$|^\+38\(\d{3}\)\d{3}\-\d{2}\-\d{2}$"
# phone_number = input("Enter number ")
# match = re.search(pattern, phone_number)
# if match != None:
#     print(match.group(0))
# else:
#     print("Incorrect number")

line = "So5465me text 255dfhfh54"
print(line)
for s in line:
    print(s)
    if s.isdigit():
        count_dig +=1