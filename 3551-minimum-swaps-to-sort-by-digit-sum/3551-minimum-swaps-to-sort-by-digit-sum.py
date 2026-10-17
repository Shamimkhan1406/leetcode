class Solution(object):
    def minSwaps(self, nums):
        def digitSum(num):
            sum = 0
            while num > 0:
                sum += num%10
                num //= 10
            return sum
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append((digitSum(nums[i]),nums[i],i))
        arr.sort(key=lambda x: (x[0], x[1]))
        visited = [False]*n
        swap = 0
        for i in range(n):
            if visited[i]:
                continue
            if i == arr[i][2]:
                visited[i]= True
                continue
            cycle = 0
            j = i
            while visited[j]!=True:
                visited[j]=True
                j = arr[j][2]
                cycle += 1
            swap += cycle - 1
        return swap
        """
        :type nums: List[int]
        :rtype: int
        """
        