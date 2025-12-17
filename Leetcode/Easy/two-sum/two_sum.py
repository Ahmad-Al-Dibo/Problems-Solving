class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        assert -10**9 <= target <= 10**9
        assert 2 <= len(nums) <= 10**4
        for x in nums:
            assert -10**9 <= x <= 10**9
        

        seen = {}
        for i, num in enumerate(nums):
            waarde = target - num
            if waarde in seen:
                return [seen[waarde], i]
            seen[num] = i

        
