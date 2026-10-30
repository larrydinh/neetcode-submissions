class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}

        for i, n in enumerate(nums):
            hash_dict[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash_dict and hash_dict[diff] != i:
                return [i, hash_dict[diff]]

        return False


