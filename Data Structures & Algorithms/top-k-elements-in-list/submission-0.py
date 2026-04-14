class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        res=[]
        sortedarr=sorted(a.items(),key=lambda x:x[1], reverse=True)

        for i in range(k):
            res.append(sortedarr[i][0])
        return res

        
        