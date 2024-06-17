class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        found_word = False
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                count+=1
                found_word=True
            elif found_word:
                break
        return count