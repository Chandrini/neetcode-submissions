class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        start=0
        maxlen=0
        for i in range(n - 1, -1, -1):      # bottom to top
            for j in range(i, n):            # left to right
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
                    if j-i+1 >maxlen:
                        start = i
                        maxlen = j - i + 1

        return s[start:start + maxlen]
