# Exercise 8.1
fh = open('mbox-short.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

# Exercise 8.2
import os

fh = None
file_input = input('Enter the file name: ')
if os.path.exists(file_input):
    fh = open(file_input)

elif file_input == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    print('File cannot be opened:', file_input)

# Exercise 8.3
def dspam():
    total = 0
    count = 0
    average = 0
    for lx in fh:
        if lx.startswith('X-DSPAM-Confidence:'):
            pl = lx.split(':')
            float_spam = float(pl[1])
            total = total + float_spam
            count = count + 1
    average = total / count
    print('Aantal:', count)
    print('Gemiddelde:', average)
    print('Totaal:', total)


if fh is not None:
    dspam()

