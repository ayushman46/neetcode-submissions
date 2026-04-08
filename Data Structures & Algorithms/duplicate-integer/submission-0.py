class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b=set(nums)
        l=len(nums)
        j=len(b)
        if j==l:
            return False
        else:
            return True