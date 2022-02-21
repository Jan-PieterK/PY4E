# Exercise 9.4
import os
all_words = []
file_input = input('Enter file:')
if os.path.exists(file_input):
    file = open(file_input)

for line in file:
    line = line.strip()
    wds = line.split()
    for word in wds:
        if word not in all_words:
            all_words.append(word)
all_words.sort()
print(all_words)

# Exercise 9.5
han = open('mbox-short1.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])

# Exercise 9.6
list = []

while True:
    str_list = input('Enter a number:')
    if str_list == 'done':
        break
    try:
        fl_list = float(str_list)
    except:
        print('Invalid input')
        continue
    list.append(fl_list)
print(list)
print(min(list), max(list))

