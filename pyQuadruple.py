//pyquadraple

i = input("How many numbers:")
i = int(i)
a = []

print("enter {0} numbers".format(i))

while i > 0:
    a.append(int(input()))
    i -= 1

a.sort()

# print(a)

mul = float(a[-1] * a[-2] * a[-3] * a[-4])

print(mul)
