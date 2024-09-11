class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1 :
            return 0
        length = 2**(n-1)
        half = length // 2
        if k<= half:
            return self.kthGrammar(n-1 , k)
        else :
            return 1 - self.kthGrammar(n-1 , k - half)     
        # 1-0= 1 , 1-1 = 0    
        