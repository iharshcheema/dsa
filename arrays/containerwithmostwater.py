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
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1  # Initialize pointers
        max_area = 0  # Variable to track the maximum area

        while left < right:
            # Calculate the area
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            
            # Update the maximum area
            max_area = max(max_area, area)
            
            # Move the pointers
            if height[left] < height[right]:
                left += 1  # Move left pointer inward
            else:
                right -= 1  # Move right pointer inward

        return max_area
    
# time complexity 0(n) since each pointer moves at most n times 
# space 0(1)





        
        