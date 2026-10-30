class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def findFinish(start1,duration1,start2,duration2):
            finish1 = float('inf')
            for i in range(len(start1)):
                finish1 = min(finish1,start1[i]+duration1[i])
            finish2 = float('inf')
            for j in range(len(start2)):
                finish2 = min(finish2,max(finish1,start2[j])+duration2[j])
            return finish2
        landFirst = findFinish(landStartTime,landDuration,waterStartTime,waterDuration)
        waterFirst = findFinish(waterStartTime,waterDuration,landStartTime,landDuration)
        return min(landFirst,waterFirst)
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        