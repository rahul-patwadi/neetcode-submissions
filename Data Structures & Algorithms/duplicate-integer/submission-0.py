class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for i in nums:
            if i not in duplicate:
                duplicate.add(i)
        if len(nums) != len(duplicate):
            return True
        else:
            return False
                