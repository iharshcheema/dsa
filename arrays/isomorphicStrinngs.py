class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        S_hasht , T_hasht = {} , {}
        for i in range (len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s not in S_hasht:
                S_hasht[char_s] = char_t

            if char_t not in T_hasht:
                T_hasht[char_t] = char_s

            if S_hasht[char_s] != char_t or T_hasht[char_t] != char_s:
                return False   
                
        return True     
