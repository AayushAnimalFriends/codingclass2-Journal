class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        BrickStacks=height
        leftmax=0
        rightmax=0
        WaterCollected=0
        leftmaxlist=list()
        rightmaxlist=list()
        for i in range(0,len(BrickStacks)):
            leftmaxlist.append(leftmax)
            if (BrickStacks[i]>leftmax):
                leftmax=BrickStacks[i]
        BrickStacks.reverse()
        for i in range(0,len(BrickStacks)):
            rightmaxlist=[rightmax]+rightmaxlist
            if (BrickStacks[i]>rightmax):
                rightmax=BrickStacks[i]
        BrickStacks.reverse()
        for i in range(0,len(BrickStacks)):
            if (min(leftmaxlist[i],rightmaxlist[i])-BrickStacks[i]>0):
                WaterCollected=WaterCollected+min(leftmaxlist[i],rightmaxlist[i])-BrickStacks[i]
            
        return WaterCollected

columns = list(map(int, input("Please Enter columns e.g 5,4,5: ").split(',')))
sol = Solution()
WaterCollected = sol.trap(columns)
print("Total water collected is", WaterCollected) 
