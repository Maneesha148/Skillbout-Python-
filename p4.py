with open('data.txt', 'r') as file:
    content = file.read()
words = content.split()
word_count = len(words)
print(f"Total number of words in data.txt file: {word_count}")