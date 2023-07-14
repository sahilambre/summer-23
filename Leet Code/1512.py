def numIdenticalPairs(nums) -> int:
    count = 0
    length = len(nums)
    for i in range(length):
        # print(i)
        for j in range(i+1, length):
            if nums[i] == nums[j]:
                count += 1

    return count

print(numIdenticalPairs([1,2,3,48,57, 1, 2]))
