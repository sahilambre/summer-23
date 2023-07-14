A = [64, 25, 12, 22, 11]

print("Initial List: ", A)
for i in range(len(A)):
    min_index = i
    
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i]
    print("Ongoing list: ", A)
print(A)