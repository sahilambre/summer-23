def numberOfDigits(number):
    flag = 0
    number = str(number)
    for element in number:
        flag += 1
    return flag

print(numberOfDigits(123))

