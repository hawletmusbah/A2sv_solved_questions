class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target > 1:
            if target % 2 == 0:
                count += 1
            else:
                count += 2
            target = target// 2
            maxDoubles -= 1
        return count + target - 1