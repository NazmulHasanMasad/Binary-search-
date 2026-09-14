class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed=1
        while True:
            totaltimes=0
            for p in piles:
                totaltimes += math.ceil(p / speed)
            if totaltimes <= h:
                return speed
            speed +=1
        return speed

       