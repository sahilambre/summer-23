#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for element in range(1,N+1):
            print("* " * element)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends\


# * 
# * * 
# * * * 
# * * * * 
# * * * * *

