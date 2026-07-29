class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        fleet=0
        for i in range(len(position)):
            speed[i]=(target-position[i])/speed[i]
            cars.append((position[i],speed[i]))
        cars.sort()
        tl=0
        for i in range(len(position)-1,-1,-1):
            p,t=cars[i]
            if t>tl:
                fleet+=1
            tl = max(tl, t)
        return fleet

        
        