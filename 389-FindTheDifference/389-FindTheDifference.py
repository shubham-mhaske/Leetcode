# Last updated: 8/15/2025, 7:52:27 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
      c=0
      for char in s: c^=ord(char)  
      for char in t: c^=ord(char)
      return chr(c)
        
        