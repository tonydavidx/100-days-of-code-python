with open('my_file.txt', 'w') as file:
    file.write('Hello')

with open("/../../../Documents/python/my_texts.txt", 'r') as file:
    text = file.read()
    print(text)
