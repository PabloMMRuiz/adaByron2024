from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()

        for i in range(len(senate)):
            if senate[i]=="R":
                radiants.append(i)
            elif senate[i] == "D":
                dires.append(i)
        
        while len(radiants)!=0 and len(dires)!=0:
            actualrad = radiants.popleft()
            actualdir = dires.popleft()
            
            if actualrad < actualdir:
                radiants.append(actualrad+len(senate))
            else:
                dires.append(actualdir+len(senate))
            
        if len(radiants)==0:
            return "Dire"
        else:
            return "Radiant"