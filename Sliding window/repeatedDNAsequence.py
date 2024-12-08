class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L = 10
        n = len(s)

        seen , output = set() , set()

        for i in range(n-L+1):
            # to get the 10 digit string from 0 to 9th index 
            string = s[i: L+i]

            if string in seen:
                output.add(string)
            seen.add(string)     
        return list(output)    

# T= 0(n) 
# S= O(n)



            



        