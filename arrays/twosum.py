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
# T = O(n^2)
# S = O(1)                
        
# in the second methos we check if the second value is in the hash table rather than traversing array      
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

# # T = O(n)
# S = O(n)
        


