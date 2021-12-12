list_1 = []
list_2 = []


file1 = open('file-1.txt', 'r')
file_1_list = file1.readlines()

file_2 = open('./file-2.txt', 'r')
file_2_list = file_2.readlines()


list_1 = [int(num.strip()) for num in file_1_list]

list_2 = [int(num.strip()) for num in file_2_list]

result = [n for n in list_1 if n in list_2]
# Write your code above 👆

print(result)
