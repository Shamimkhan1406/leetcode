class Solution(object):

    def minimumChanges(self, s, k):

        n = len(s)
        INF = 10**9

        # cost[l][r] = minimum changes needed
        # to make s[l:r+1] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        # --------------------------------
        # Precompute cost for every substring
        # --------------------------------
        for l in range(n):

            for r in range(l + 1, n):

                length = r - l + 1

                # Try every proper divisor
                for d in range(1, length):

                    if length % d != 0:
                        continue

                    changes = 0

                    for start in range(d):

                        left = l + start
                        right = l + start + (length // d - 1) * d

                        while left < right:

                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[l][r] = min(cost[l][r], changes)

        # --------------------------------
        # Partition DP
        # --------------------------------

        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):

            # Need at least 2 characters per part
            for i in range(2 * parts, n + 1):

                # j = starting position of last substring
                for j in range(2 * (parts - 1), i - 1):

                    if dp[parts - 1][j] == INF:
                        continue

                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
"""
        :type s: str
        :type k: int
        :rtype: int
"""
        