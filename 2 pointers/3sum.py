# brute force 
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        # Sort the array to handle duplicates and ensure order
        nums.sort()

        # Iterate through all triplets
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:  # Use == for comparison
                        triplet = [nums[i], nums[j], nums[k]]
                        if triplet not in res:  # Ensure unique triplets
                            res.append(triplet)
        
        return res
    
    # T= O(n3) 



# Two pointer approach 
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()

        # first pointer has to go through length of nums, that is pointing towards the current fixed element 
        for i in range(n):
            if i==0 or nums[i-1] != nums[i]:

                # two sum II 
                # these two pointers will be for the two sum approach 
                left = i + 1 
                right = n - 1
                target = -nums[i]
                while left < right:
                    currentSum = nums[left] + nums[right]
                    if currentSum == target:
                        triplet = [nums[i] , nums[left] , nums[right]]
                        res.append(triplet)
                        # for the current value of i(current fixed element), we want to check if more triplets exists 
                        left +=1
                        # [1,2,2...] , we want to skip the second 2
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                    elif currentSum < target :
                        left+=1
                    else:
                        right-=1  
        return res       

    T = O(n2)            


    
