# Exercise 5.6
def computepay(hours, rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay


sh = input("enter Hours: ")
sr = input("enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("pay:", xp)

# Exercise 5.7
score_str = input("Enter score: ")


def computegrade():
    try:
        score_int = float(score_str)
    except:
        print("Bad score")
        return
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


computegrade()

