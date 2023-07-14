def maxmimumWealth(accounts):
    maxWealth = 0
    for i in range(len(accounts)):
        wealth = 0
        for j in range(len(accounts[i])):
            wealth += accounts[i][j]

        if wealth > maxWealth:
            maxWealth = wealth
    
    return maxWealth

print(maxmimumWealth([[1,2,3],[5,6,7]]))