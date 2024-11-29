class Solution(object):
    def reverse(self, array, start, end ):
        # phla element ek index age jara aur last element ek index piche ara to phla element surpass na krde uske liye while loop 
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

# Why are we using self in your code?
# In your Solution class:

# self.reverse:
# This refers to the reverse method defined in the Solution class.
# By writing self.reverse(array, 0, len(array) - 1), you are calling the reverse method of the same instance.
# Without self, Python would not know where to find the reverse method, because it assumes functions without self are either local to the method or globally defined.




# How the Code Works with self:
# You define a class Solution with two methods:

# reverse to reverse a portion of the array in-place.
# rotate to rotate the array by k steps.
# Inside rotate, you call the reverse method using self.reverse to reverse parts of the array in sequence.

# For example, in this line:

# self.reverse(array, 0, len(array) - 1)
# self ensures that Python looks for reverse in the Solution instance


# Time complexity 
# The time complexity of the rotate function using the reverse method is O(n)