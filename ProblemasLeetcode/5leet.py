#el 255 de acepta el reto era indicar la longitud de la substr mas larga en esta es devolver esta substr
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ""
        res = ""
        for i in range(len(s)):
            sub = s[i]
            k = 1
            while i+k<len(s) and s[i] == s[i+k]:
                sub+=s[i+k]
                k+=1
            k-=1
            j=1
            while i-j >=0 and i+k+j < len(s):
                if s[i-j] == s[i+k+j]:
                    sub = s[i-j] + sub + s[i-j]
                    j+=1
                else:
                    break
            if len(sub) > len(res):
                res = sub
        return res