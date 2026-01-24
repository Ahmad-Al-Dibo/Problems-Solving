class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        maps={}
        for i, num in enumerate(nums):
            if num not in maps:
                maps[num] = 1
            elif num in maps:
                maps[num] += 1
        bigstnum = 0
        bigstindex = None
        for i in maps:
            if maps[i] > bigstnum:
                bigstnum = maps[i]
                bigstindex = i
        return bigstindex

        
