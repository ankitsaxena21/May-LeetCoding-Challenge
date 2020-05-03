class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=set(ransomNote)
        for i in r:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
