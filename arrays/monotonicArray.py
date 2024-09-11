class Solution(object):
    def isMonotonic(self, array):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        n = len(array)
        if n == 0:
            return True
        first = array[0]
        # if length is 5 then last element will be at 4th index 
        last =  array[n-1]
        if first > last :
            # it can be either monotonic decreasing or non monotonic 
            for value in range(n-1):
                if array[value] < array[value+1]:
                    return False

        elif first == last:
            # array can be monotonic if all values r equal 
            for value in range(n-1):
                if array[value]!= array[value+1]:
                    return False
        else:
            # first < last
            # it can be monotonic increasing or non monotonic 
            for value in range(n-1):
                if array[value] > array[value+1]:
                    return False
        return True            
