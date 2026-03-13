class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val
        
       
        res = []
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            
            original_pos = ord(s[i]) - ord('a')

            new_pos = (original_pos + current_shift) % 26
            res.append(chr(ord('a') + new_pos))
            
        return "".join(res)