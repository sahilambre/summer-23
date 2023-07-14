def pattern(N):
    for element in range(N, 0, -1):
        for newElement in range(1, element + 1):
            print(newElement, end=" ")
        print()

# pattern(5)


print(pattern(5))