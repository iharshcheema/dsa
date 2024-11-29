class Solution(object):
    def sortedSquares(self, array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resultArray= [0]*len(array)
        for i in range(len(array)):
            resultArray[i]= array[i]**2
        resultArray.sort()
        return resultArray    

# time complexity is nlogn because any sorting has time complexity of nlogn and to raverse while squaring is n and n+ nlogn is nlogn 

# Method 2 : 

class Solution(object):
    def sortedSquares(self, array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j = len(array) - 1
        resultArray= [0]*len(array)
        for item in reversed(range(len(array))):
            if array[i]**2> array[j]**2:
                resultArray[item] = array[i]**2
                i = i+1
            else :
                resultArray[item] = array[j]**2
                j = j-1
        return resultArray        

            
        
        

        
        
        

        
        