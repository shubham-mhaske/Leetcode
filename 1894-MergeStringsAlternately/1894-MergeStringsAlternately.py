# Last updated: 8/15/2025, 7:52:26 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        result = []
        while i < len(word1) or i < len(word2):
            if i< len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        
            i+=1
        return ''.join(result)        