class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        answer = 1
        l = len(s)
        if l == 1:
            return answer
        positions_map = {}
        start = 0
        positions_map[s[0]] = 0
        currLen = 1
        for i in range(1,l):
            if s[i] in positions_map and positions_map[s[i]]!=-1:
                pos = positions_map[s[i]]
                for j in range(start,pos+1):
                    positions_map[s[j]] = -1
                currLen = currLen - (pos-start+1)
                start = pos+1
            positions_map[s[i]] = i
            currLen += 1
            answer = max(answer,currLen)
        return answer
