class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        ops = 0
        for char in blocks[0:k]:
            if char == "W":
                ops+=1
        bestOp = ops
        while i+k<len(blocks):
            left = blocks[i]
            right = blocks[i+k]
            if left == "W":
                ops -=1
            if right == "W":
                ops += 1
            if ops < bestOp:
                bestOp = ops
            i+=1
        return ops
