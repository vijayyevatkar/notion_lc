class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        inp = sorted(intervals, key=lambda x: x[0])
        
        answer = []
        prev = inp[0]
        for i in range(1,len(inp)):
            curr = inp[i]
            if (prev[1] >= curr[0] and prev[1] <= curr[1]) or (curr[0]<=prev[1]):
                prev = [prev[0], max(prev[1],curr[1])]
                # print(prev)
            else:
                answer.append(prev)
                prev = curr
        answer.append(prev)
        return answer