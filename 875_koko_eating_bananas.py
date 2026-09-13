class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        res=r

        while l <= r:
            k= (l+r)//2
            hours=0
            for p in piles:
                hours += Math.ceil(float(p)/k)
            if hours <= h:
                res= k
                r=k-1
            else:
                l=K+1
        return res



#time complexity 0(m * log(n))
#space complexity 0(1)

