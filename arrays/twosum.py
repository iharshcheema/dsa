# Inner Loop and Outer Loop in Python

# Python loops are used to iterate over sequences or ranges. When nested loops (a loop inside another loop) are used, they consist of:

# Outer Loop: The primary loop that controls the number of times the inner loop runs.
# Inner Loop: Executes completely for each iteration of the outer loop.
# Example of Inner and Outer Loop:

# for i in range(3):  # Outer loop
#     for j in range(2):  # Inner loop
#         print(f"Outer loop: {i}, Inner loop: {j}")

# How it works:

# The outer loop starts its first iteration (i = 0).
# The inner loop runs fully (j = 0, 1) for each iteration of the outer loop.
# Once the inner loop completes, the outer loop moves to the next iteration (i = 1), and so on.

# Output:

# Outer loop: 0, Inner loop: 0
# Outer loop: 0, Inner loop: 1
# Outer loop: 1, Inner loop: 0
# Outer loop: 1, Inner loop: 1
# Outer loop: 2, Inner loop: 0
# Outer loop: 2, Inner loop: 1










# two sum 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(i+1 , len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i,j]
        return []  

# Explanation:
# Outer Loop (for i in range(0, len(nums) - 1):):

# This loop picks the first number nums[i] from the list nums.
# It starts from index i = 0 and goes up to the second last index (len(nums) - 1).
# Inner Loop (for j in range(i + 1, len(nums)):):

# For each i, the inner loop iterates through the numbers after index i (j = i + 1) to find a pair.
# This ensures that every combination of two numbers in the list is checked once.
# Condition (if nums[i] + nums[j] == target:):

# Checks if the sum of the two numbers nums[i] and nums[j] equals the given target.
# Return Indices (return [i, j]):

# If a pair is found that sums up to the target, the function immediately returns their indices [i, j].
# Return Empty List (return []):

# If no such pair is found after all iterations, the function returns an empty list.

# # T = O(n^2)
# S = O(1)                





        
# in the 2 METHOD we check if the second value is in the hash table rather than traversing array      
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary ={}
        for i in range(len(nums)):
            required_value = target - nums[i] 
            if required_value in dictionary:
                return [i, dictionary[required_value]]
            else:
                # hum dictionary ki key mai current item ki value save krre aur us dictionary ki key ki value current item ka index hai 
                dictionary[nums[i]]=i    
# what we r gonna do is we ll create an dictionary aur us dinctionary k key m hum array ki value store krege aur us value ka index dictionary k us key ki value m  

# hum phle required value calculate krlege and after that hum hashtable m dhundege value agr milgi toh hashtable se us key ki value dedege agr ni mili toh hashtable ki key m current array element store krdege aur value m current element ka index 

# T = O(n)
# S = O(n)
        


