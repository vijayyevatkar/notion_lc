class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        store = [l+10]*26
        
        for i in range(l):
            store_index = ord(s[i])-97
            if store[store_index] == l+10:
                store[store_index] = i
            elif store[store_index] >= 0 and store[store_index]<l:
                store[store_index] = l+237
                
        answer = min(store)
        if answer >= l:
            answer = -1
        return answer
                