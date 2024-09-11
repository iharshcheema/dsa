class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def josephus(n, k):
            # Base case: only one person left
            if n == 1:
                return 0
            else:
                # Recursive case: The position returned by josephus(n-1, k) is adjusted
                return (josephus(n - 1, k) + k) % n
        
        # Call the recursive Josephus function and adjust for 1-based indexing
        return josephus(n, k) + 1


# iterative approach 
def findTheWinner(self,n, k):
    survivor = 0
    for i in range(2,n+1):
        survivor = (survivor + k) % i
    return survivor + 1    