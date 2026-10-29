class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(n):
            for j in range(m):
                land_first_finish = landStartTime[i]+landDuration[i]
                water_finish = max(land_first_finish,waterStartTime[j]) + waterDuration[j]

                water_first_finish = waterStartTime[j]+waterDuration[j]
                land_finish = max(water_first_finish,landStartTime[i])+landDuration[i]
                
                ans = min(ans,water_finish,land_finish)
        return ans
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        