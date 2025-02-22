

#відкрити файл
#читати файл
#записати файл
#закрити файл

#absolute path
url = r'C:\Users\helen\Desktop\NewGroups\05_Python_SPR_411\16_Files\test.txt'
#відностий шлях до файлу
#file = open('./16_Files/test.txt')
#file = open(url)

#read all lines
#print(file.read())

#read one line
# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())

#read all lines - add to list
#print(file.readlines())

#real all lines
# print(file.read(5))

# file.close()


# with open(url) as file: #file = open(url)
#     print(file.read())
#     # file.close()

# #'w' - режим перезапису файлу
# url_to_write = "./16_Files/write_file.txt"
# with open(url_to_write, 'w') as file:
#     file.write("Hello friend")

#'a' - режим дозапису файлу
# url_to_write = "./16_Files/write_file.txt"
# with open(url_to_write, 'a') as file:
#     file.write("Hello friend\n")

lines = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
'Donec ac nunc convallis, sollicitudin tellus accumsan, dignissim augue.',
'In eleifend nisi eget ligula viverra, non posuere erat pharetra.',
'Nulla vitae justo finibus, pretium nisl et, laoreet dui.'
]

# url_to_write = "./16_Files/write_file.txt"
# with open(url_to_write, 'w') as file:
#     #file.write(lines)
#     counter = 1
#     for line in lines:
#         file.write(f"{counter}. {line}\n")
#         counter+=1

# url_to_write2 = "./16_Files/write_file_somehow.txt"
# with open(url_to_write2, 'w') as file:
#     file.writelines(lines)

def readFile(file_name):
    with open(file_name,'r') as file:
        read_line = file.read()
        return read_line
  
def writeFile(file_name, info):
    with open(file_name,'a') as file:
        file.write(info)

url_read = "./16_Files/test.txt"
url_write = "./16_Files/write_file.txt"

# text = readFile(url_read)
# writeFile(url_write, text)

with open(url_read,'r') as file:
    read_lines = file.readlines()
        
# for line in lines[::-1]:
#     print(line)

# with open(url_write,'a') as file:
#     for line in lines[::-1]:
#         file.write(line+'\n')
    
with open(url_write,'w') as file:
    print(file.writable())
    print(file.readable())