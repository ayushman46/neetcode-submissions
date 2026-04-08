class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in a:
                return [a[rem],i]
            else:
                a[num]=i


