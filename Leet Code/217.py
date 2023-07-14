def containsDuplicate(nums):
    # pass
    for element in nums:
        # print(element)
        if element in nums:
            return True
        else:
            return False

print(containsDuplicate([1,2,3,5,3]))
print(containsDuplicate([1,2,3,5,4]))