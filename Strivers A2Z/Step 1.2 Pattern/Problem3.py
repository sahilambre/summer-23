def trianglePattern(N):
    for element in range(1,N+1):
        # print(element)
        for newElement in range(1,element+1):
            print(newElement, end=" ")
        print()
print(trianglePattern(5))

print("Welcome to", end=' ')
print("GeeksforGeeks")