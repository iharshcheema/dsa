class Solution(object):
    def reverse(self, array, start, end ):
        # phla element ek index age jara aur last element ek index piche ara to phla element surpass na krde 
        while(start<end):
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
            
        return array    

    def rotate(self, array, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5], k=3
        k = k % len(array)
        self.reverse(array , 0 , len(array)-1 )
        # [5,4,3,2,1]
        self.reverse(array , 0 , k-1 )
        # [3,4,5,2,1]
        self.reverse(array , k , len(array)-1 )
        [3,4,5,1,2]
