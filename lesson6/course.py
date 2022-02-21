# Exercise 6.1
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
print(tot, num, tot/num)

# Exercise 6.2
count = 0

while True:
    input_val = input('Enter a number: ')
    if input_val == 'done':
        break
    try:
        val = float(input_val)
    except:
        print('not a Number')
        continue
    if val > count:
        count = val
    print(count, val)


count = None

while True:
    input_val = input('Enter a number: ')
    if input_val == 'done':
        break
    try:
        val = float(input_val)
    except:
        print('not a Number')
        continue
    if count == None:
        count = val
    elif val < count:
        count = val
    print(count, val)
