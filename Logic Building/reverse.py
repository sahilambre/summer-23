def reverse(number):
    reverse_number = 0
    while (number > 0):
        remainder = number % 10
        reverse_number = (reverse_number * 10) + remainder
        number = number // 10
    return reverse_number
print(reverse(12345))

# to check if a number is a palindrome

def palindromeNo(number):
    original_number = number
    reverse_number = 0
    while (number > 0):
        remainder = number % 10
        reverse_number = (reverse_number * 10) + remainder
        number = number // 10
    if original_number == reverse_number:
        return True
    else:
        return False
    # return reverse_number
print(palindromeNo(12345))
print(palindromeNo(12321))

# check for base case 