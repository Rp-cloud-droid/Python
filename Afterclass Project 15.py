new_file = open('Afterclass Project.txt', 'x')
file = open('Afterclass Project.txt', 'w')
file.write("Hi! This is Afterclass Project")
file.close()

file1 = open('Afterclass Project.txt', 'r')
print(file1.read())
file1.close()