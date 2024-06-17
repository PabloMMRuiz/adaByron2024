class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        
        for i in range(n - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            if bit_sum > 1:
                carry = 1
                res = str(bit_sum % 2) + res
            else:
                carry = 0
                res = str(bit_sum) + res
        
        if carry==1:
            res = '1' + res
        
        return res


