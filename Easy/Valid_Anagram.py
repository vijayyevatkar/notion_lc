class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sDict = self.buildCountDictionary(s)
        tDict = self.buildCountDictionary(t)

        return self.checkSourceInTarget(sDict,tDict) and self.checkSourceInTarget(tDict,sDict)

    def buildCountDictionary(self, s: str) -> dict:
        countOfS = {}
        for ch in s:
            if ch in countOfS:
                countOfS[ch] += 1
            else:
                countOfS[ch] = 1

        return countOfS

    def checkSourceInTarget(self, source: dict, target: dict) -> bool:

        for k,v in source.items():
            if k not in target:
                return False
            if v != target[k]:
                return False

        return True