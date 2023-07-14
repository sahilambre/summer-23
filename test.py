def findMedianSortedArrays(nums1, nums2):
    new_list = nums1 + nums2
    # return new_list
    #sorting logic
    #?bubble sort 
    # swapped = False
    n = len(new_list)

    for i in range(n):
        swapped = False
        for j in range(0, n -i -1):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
                swapped = True
        if swapped == False:
            new_length = len(new_list)
            #?mediam logic
            if new_length % 2 == 0:
                mid = new_length // 2
                result = (new_list[mid] + new_list[~mid]) / 2
                return result
                # return the average of two middle element
            else:
                #return the middle element
                middle_index = (new_length - 1) // 2
                return new_list[middle_index]

print(findMedianSortedArrays([2,2,4,4], [2,2,4,4]))

'''
In Python, the "~" operator is the bitwise complement operator, 
not the negation operator. It performs a bitwise negation of the operand, 
which means it flips all the bits of the operand.

In your code, when you use the expression "~mid", 
it calculates the bitwise complement of the value stored in the variable "mid". 
The value of "mid" is 3, which is represented in binary as "00000011" 
(assuming 8-bit representation). 
When you apply the bitwise complement operator to it, you get "11111100" in binary, 
which is the two's complement representation of -4 in decimal.
'''