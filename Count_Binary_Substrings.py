class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        l = len(s)
        if l==1:
            return 0
        
        answer = 0
        prev = 0
        curr = 1
        for i in range(1,l):
            if s[i]==s[i-1]:
                curr+=1
            else:
                answer += min(prev,curr)
                prev, curr = curr, 1
        answer += min(prev,curr)
        return answer
                