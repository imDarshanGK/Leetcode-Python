class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin1 = int(a,2)
        bin2= int(b,2)
        sum_of_binary = bin1+bin2
        return bin(sum_of_binary)[2:]
        result = addBinary(a,b)
        print(result)
