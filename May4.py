class Solution:
    def findComplement(self, num: int) -> int:
        bin = self.getBinary(num)
        ans = ""
        for i in str(bin):
            if i == "0":
                ans = ans + "1"
            else:
                ans = ans + "0"
        return self.binaryToDecimal(int(ans))
    
    def getBinary(self, n: int) -> int:
        return bin(n)[2:]
            
    
    def binaryToDecimal(self, bin: int) -> int: 
        binary1 = bin 
        decimal, i, n = 0, 0, 0
        while(bin != 0): 
            dec = bin % 10
            decimal = decimal + dec * pow(2, i) 
            bin = bin//10
            i += 1
        return decimal
