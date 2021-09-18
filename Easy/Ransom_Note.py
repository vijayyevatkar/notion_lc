class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNoteCountList = self.buildCharCount(ransomNote)
        magazineCountList = self.buildCharCount(magazine)
        
        for i in range(26):
            if ransomNoteCountList[i] > magazineCountList[i]:
                return False
        
        return True
    
    
    def buildCharCount(self, s: int) -> List[int]:
        
        answer = [0]*26
        for ch in s:
            index = ord(ch)-97
            answer[index] += 1
        return answer
        