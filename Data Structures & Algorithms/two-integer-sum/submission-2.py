class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for i,num in enumerate(nums):
            a=target-num
            if a in count:
                return [count[a],i]
            else:
                count[num]=i
        
                
        