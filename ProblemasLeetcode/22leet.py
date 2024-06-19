class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def bt(left, right, s):
            if left == n and right == n:
                res.append(s)
                return
        
            if left<n:
                bt(left+1,right,s+"(")
            
            if right<left:
                bt(left,right+1,s+")")
        
        bt(0,0,"")
        return res