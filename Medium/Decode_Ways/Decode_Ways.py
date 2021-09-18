class Solution:
    def numDecodings(self, s: str) -> int:
        
        # First check that all the zeroes are in right places.
        if not self.checkValidityWithZero(s):
            return 0

        l = len(s)
        # dp = [1]*(l+1)
        n2 = 1
        n1 = 1

        for i in range(1,l):
            curr = int(s[i])
            prev = int(s[i-1])
            val = prev*10+curr
            # print(f"curr, prev, val are: {curr}, {prev}. {val}")
            if val > 26:
                n2 = n1
            else:
                if curr == 0:
                    n1,n2 = n2,n1
                elif val > 0 and val < 10:
                    n2 = n1
                else:
                    # dp[i] = dp[i-1]+dp[i-2]
                    n2, n1 = n1, n1+n2
            # print(f"dp[{i}] id {dp[i]}")

        return n1

    def checkValidityWithZero(self, s: str) -> bool:

        l = len(s)
        if s[0] == "0":
            return False
        for i in range(1,l):
            if s[i] == "0" and (int(s[i-1]) > 2 or s[i-1]=="0"):
                return False
        return True
