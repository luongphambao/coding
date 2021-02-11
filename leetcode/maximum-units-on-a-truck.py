class Solution:
    def maximumUnits(self, boxes: List[List[int]], truck: int) -> int:
        boxes=sorted(boxes,key=lambda x:x[1],reverse=True)
        # sắp xếp giảm dần dựa trên unitbox
        count=0
        for a,b in boxes:
            if truck-a>=0:
                count+=a*b
                truck-=a
            else:
                count+=b*truck
                break
        return count