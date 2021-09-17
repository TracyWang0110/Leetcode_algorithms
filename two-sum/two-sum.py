class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                # nums = [3,2,4], target = 6
        dic = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in dic:
                return [dic[goal], i]
            else:
                dic[nums[i]] = i