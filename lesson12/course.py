# # Exercise 12.1
import re
file = input('Enter a file name: ')
r = input('Enter a regular expression: ')

count = 0
opened_file = open(file)
for line in opened_file:
    line = line.strip()
    if re.search(r, line):
        count += 1

print("mbox-short0.txt has", count, "lines that matches the regular expression")

# Exxercise 12.2
file = open('mbox-short0.txt')
count = 0
number = 0
averege = 0
for line in file:
    word = re.findall("^[N-zA-Z]+ [R-zA-Z]+: [0-9]+$", line)
    if len(word) == 0:
        continue
    word = list(map(lambda x: x.split(': ')[-1], word))  # get number
    str_number = ' '.join([str(elem) for elem in word])  # convert list to string
    int_number = int(str_number)  # set to integer
    count += int_number
    number += 1
averege = count / number
print(count)
print(number)
print(averege)





