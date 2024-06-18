class Solution:
    
    def backtrack(self,idx, comb, solutions,digits):
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if idx == len(digits):
            solutions.append(comb)
            return
            
        for letter in digit_to_letters[digits[idx]]:
            self.backtrack(idx + 1, comb + letter,solutions,digits)

    def letterCombinations(self, digits: str) -> List[str]:
        #genetico si hombre
        if not digits:
            return []
        res = []
        self.backtrack(0, "",res,digits)
        return res