class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        print(nums)
        max_len = 1
        longest_len = 1
        if len(nums)==0:
            return 0
        for idx in range(len(nums)-1):
            print("compare", nums[idx]+1,nums[idx+1])
            if (nums[idx]+1 == nums[idx+1]):
                longest_len+=1
                max_len = max(max_len, longest_len)
                print("max_len", max_len)
            else:
                longest_len = 1
        return max_len


