# Exercise 11
fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

x = list()
for k, v in di.items():
    newt = (v, k)
    x.append(newt)

x = sorted(x, reverse=True)

for v, k in x[:5]:
    print(v,k)

# Exercise 11.1
file = 'mbox.txt'
opened_file = open(file)

di = {}
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

# Exercise 11.2
file = 'mbox-short0.txt'
opened_file = open(file)

di = {}

for line in opened_file:
    if line.startswith("From "):
        time = line.split()[5]
        hours = time.split(':')[0]
        di[hours] = di.get(hours, 0) + 1
print(di)

items = list(di.items())
items.sort()
print(items)

for x in items:
    print(x[0], x[1])

# Exercise 11.3

file = 'mbox.txt'
lower_file = open(file)
di = {}
for line in lower_file:
    for letter in line:
        letter = letter.lower()
        if letter.isalpha():
            di[letter] = di.get(letter, 0) + 1

b = dict(sorted(di.items(), key=lambda item: item[1], reverse=True))
print(b)