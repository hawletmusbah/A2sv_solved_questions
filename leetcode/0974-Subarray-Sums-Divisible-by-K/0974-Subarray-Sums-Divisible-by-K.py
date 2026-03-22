class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_freq = {0 : 1}
        result = 0
        tempo = 0
        for char in nums:
            tempo += char
            rem = tempo % k
            if rem in count_freq:
                result += count_freq[rem]
                count_freq[rem] += 1

            else:
                count_freq[rem] = 1
        return result