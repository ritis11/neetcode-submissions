class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_={}
        for i, val in enumerate(nums):
            ele = dict_.get(val, None)
            if ele is None:
                dict_[val] = i
            else:
                return True
        return False
        