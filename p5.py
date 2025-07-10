with open('data.txt', 'w') as file:
    file.write("Hello, this is the first line.\n")
with open('data.txt', 'a') as file:
    file.write("This is the second line added.\n")
with open('data.txt', 'r') as file:
    content = file.read()
    print("File Content:\n")
    print(content)
