"""
Write a function which will work out the check digit
for a stream of integers using the mod 11 method.

Remember - weighting starts from 2 at the end digit.
"""

def checkDigitFunc(ds):
    multipliedWeight = 0
    c=2
    for i in range(len(ds)-1,-1,-1):
        multipliedWeight += int(ds[i]) * c
        c+=1
    checkDigit = 11-(multipliedWeight % 11)
    return checkDigit

while True:
    digitStream = str(input("Enter a stream of integers: "))
    if len(digitStream) > 11:
        print("Must be 11 or less digits")
    else:
        print("Check digit: ", checkDigitFunc(digitStream))
