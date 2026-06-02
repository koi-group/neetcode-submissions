class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mas = []
        for i in nums:
            if i in mas:
                return True
            else:
                mas.append(i)
        return False