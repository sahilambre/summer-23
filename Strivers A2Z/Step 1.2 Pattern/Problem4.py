def triangleProblem(N):
    for element in range(1, N+1):
        for newElement in range(1, element + 1):
            print(element, end=" " )
        print()

print(triangleProblem(5))