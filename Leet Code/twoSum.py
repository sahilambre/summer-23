def twoSum(nums, target)->int:
    n = len(nums)
    two_sum = []
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                two_sum.append(i)
                two_sum.append(j)

                return two_sum
    # return two_sum


print(twoSum([1,2,3,4,5], 6))