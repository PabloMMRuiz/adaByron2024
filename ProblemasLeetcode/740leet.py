from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a1,a2 =0,0 #valores anteriores con los q comparamos, a1 es el anterior al anterior y a2 el anterior
        count = Counter(nums)
        nums = sorted(set(nums))
        for i in range(len(nums)):
            valori = nums[i]*count[nums[i]]

            #si se cumple la condición , no podemos sumar el siguiente asi que solo comparamos entre el anterioralanterior+actual y anterior
            if i>0 and nums[i]==nums[i-1]+1:
                a1,a2=a2,max(a1+valori,a2)
            else:
                a1,a2=a2,a2+valori
        return a2