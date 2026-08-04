class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        sorted_num=sorted(a.items(),key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_num[:k]]