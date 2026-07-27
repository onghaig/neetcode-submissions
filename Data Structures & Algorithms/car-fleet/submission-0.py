class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we need to update position constantly, use that to track
        cars = [[p, s] for p, s in zip(position, speed)]
        # [  [pos, speed]  ]
        
        cars.sort(key = lambda car: car[0], reverse=True)

        # so now we have cars that are sorted by decreasing position
        # [[1,4],[3,2]]
        times = []
        for car in cars:
            time = (target - car[0])/car[1]
            if len(times) == 0:
                times.append(time)
            if (time > times[-1]):
                times.append(time)
            
        return len(times)

            