class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0]*len(prices)
        minimun=prices[0]
        for i in range(1, len(prices)):
            if prices[i]-minimun > dp[i-1]:
                dp[i]=prices[i]-minimun
            else:
                dp[i] = dp[i-1]
            if prices[i]<minimun:
                minimun = prices[i]
        return dp[len(prices)-1]
