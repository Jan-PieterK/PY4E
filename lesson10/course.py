# Exercise 10.2
file = input('Enter a file name:')

di = {}

if file == 'mbox-short0.txt':
    opened_file = open(file)

try:
    for line in opened_file:
        if line.startswith('From '):
            word = line.split()[2]
            di[word] = di.get(word, 0) + 1
    print(di)

except:
    print('File not found')

# Exercise 10.3
file = input('Enter a file name:')

di = {}

if file == 'mbox-short0.txt':
    opened_file = open(file)

try:
    for line in opened_file:
        if line.startswith('From '):
            word = line.split()[1]
            di[word] = di.get(word, 0) + 1
    print(di)

except:
    print('File not found')

# Exercise 10.4
file = input('Enter a file name:')
di = {}

if file == 'mbox-short0.txt':
    opened_file = open(file)

try:
    most_message = None
    number_message = 0
    for line in opened_file:
        if line.startswith('From '):
            word = line.split()[1]
            di[word] = di.get(word, 0) + 1
    for mail_adress in di:
        if di[mail_adress] > number_message:
            most_message = mail_adress
            number_message = di[mail_adress]
    print(most_message, number_message)

except:
    print('File not found')


# Exercise 10.5
file = input('Enter a file name:')

di = {}

if file == 'mbox-short0.txt':
    opened_file = open(file)

try:
    for line in opened_file:
        if line.startswith('Author: '):
            word = line.split('@')[1]
            di[word] = di.get(word, 0) + 1
    print(di)

except:
    print('File not found')
