class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

    # DP array
        dp = [0] * n

    # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

    # Fill DP
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]