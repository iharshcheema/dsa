# Method 1 
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ 
        # assumed max area 
        max_area = 0

        # n will be equal to a integer that is equal to the number of elements present in the array 
        n = len(height)

        for i in range(n):
            for j in range(i+1 , n):
                 width = j-i
                 minheight = min(height[i], height[j])

                 area = width*minheight

                 max_area= max( area , max_area)

        return max_area  
    
    # time comp O(n^2)





# Method 2 



        
        