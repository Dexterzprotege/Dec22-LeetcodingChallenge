# Question: https://leetcode.com/problems/minimum-average-difference/

# Solution:
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        sumFront, sumEnd = 0, sum(nums)
        ans, diff = 0, 99999
        
        for i in range(n):
            sumFront += nums[i]
            sumEnd -= nums[i]
            
            avg1 = sumFront // (i+1)
            avg2 = 0
            if i != n-1:
                avg2 = sumEnd // (n-i-1)
            
            if abs(avg1-avg2) < diff:
                diff = abs(avg1-avg2)
                ans = i
        
        return ans
