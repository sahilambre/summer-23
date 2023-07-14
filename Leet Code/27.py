def removeElement(nums, val):
    count = len(nums)
    pointer = 0
    while pointer < len(nums):
        if nums[pointer] == val:
            count = count - 1
        pointer = pointer + 1
    
    return count

    # return len(nums)

print(removeElement([3,2,2,3], 2))