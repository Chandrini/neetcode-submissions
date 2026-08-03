class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        n = len(nums)

    # DP array
        dp = [0] * (n-1)

    # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

    # Fill DP
        for i in range(2, n-1):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        dp1 = [0] * (n-1)

    # Base cases
        dp1[0] = nums[1]
        dp1[1] = max(nums[1], nums[2])

    # Fill DP
        for i in range(2, n-1):
            dp1[i] = max(dp1[i - 1], nums[i+1] + dp1[i - 2])


        return max(dp1[-1],dp[-1]) 