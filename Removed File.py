file1 = open('Codingal Updated.txt', 'r')
file2 = open('Codingal Updated.txt', 'w')

for line in file1.readlines():

    if not (line.startswitch('Coding')):

        print(line)

        file2.write(line)

file2.close()
file1.close()