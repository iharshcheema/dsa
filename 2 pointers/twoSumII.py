class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]  # 1-based index
            elif currentSum < target:
                left += 1  # Move left pointer to increase sum
            else:
                right -= 1  # Move right pointer to decrease sum

# T = 0(n) 

# S = O(1)  # Space complexity is constant because we only use a few variables.

# Explanation:
# while left < right ensures the loop runs as long as left and right pointers don't cross.
# Inside the loop:
# If the sum matches the target, return the indices (1-based).
# If the current sum is less than the target, increment left to increase the sum.
# If the current sum is greater than the target, decrement right to decrease the sum.