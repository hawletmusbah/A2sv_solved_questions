class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # uncovered = set(houses) - set(heaters)
        # ranges = [ [ heater , heater ] for heater in heaters]
        # raidus = 0
        # while uncovered :
        #     raidus += 1
        #     for each in ranges:
        #         each[0] -= 1
        #         each[1] += 1
        #         uncovered.discard(each[0])
        #         uncovered.discard(each[1])
        # return raidus

        def mindistance(heaters,house):
            l ,r = 0 , len(heaters)- 1
            min_dis = float('inf')
            while l <= r:
                mid = (l + r) // 2 
                min_dis = min (min_dis , abs(heaters[mid] - house))
                if heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid - 1

            return min_dis
        radius = 0
        heaters.sort()
        for house in houses:
            radius = max(radius, mindistance(heaters,house))
        return radius