class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum( nums[0:k] )
        max_sum = curr_sum

        for i in range(k,len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]

            max_sum = max(curr_sum , max_sum)

        return max_sum/float(k)   

# time complexity is O(n) because we are running a single loop through the array once.
# firstly we have to do k operations then n-k operartions which is n operations at the end 

# Integer Division: If you are using Python 2, the division max_sum / k will perform integer division instead of floating-point division, which may lead to incorrect results. For example, 5 / 2 will return 2 instead of 2.5. To fix this, explicitly make k a float or use from __future__ import division at the top of the file.