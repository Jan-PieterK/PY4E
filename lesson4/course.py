# Exercise 3.1
sh = input("enter Hours: ")
sr = input("enter Rate: ")
fh = float(sh)
fr = float(sr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("pay:", xp)

# Exercise 3.2
sh = input("enter Hours: ")
sr = input("enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("pay:", xp)

# Exercise 3.3
score_str = input("Enter score: ")
try:
    score_int = float(score_str)
except:
    print("Bad score")
    quit()
if score_int >= 0.9:
    print("A")
    quit()
if score_int >= 0.8:
    print("B")
    quit()
if score_int >= 0.7:
    print("c")
    quit()
if score_int >= 0.6:
    print("D")
    quit()
if score_int < 0.6:
    print("F")


