class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        previous = set()
        for i in nums:
            if i in previous:
                return True
            previous.add(i)
        return False