class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        c = 0
        for i in S:
            if i in jewels:
                c=c+1
        return c
