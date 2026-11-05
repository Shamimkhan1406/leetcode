class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count= 0
        arr2.sort()
        for num in arr1:
            i = 0
            j = len(arr2)
            while i < j:
                m = i+(j-i)//2
                if arr2[m]<num:
                    i+=1
                else:
                    j-=1
            if i<len(arr2) and arr2[i]-num<=d:
                continue
            if i > 0 and num-arr2[i-1]<=d:
                continue
            count += 1
        return count
            
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        