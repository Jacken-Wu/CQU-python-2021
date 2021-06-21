with open('data.txt') as f:

    for line in f.readlines():
        line = line.strip('\n')
        print(line)
f.close()

