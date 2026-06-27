class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = (set(nums))
        length = 0
        for num in nums:
            if (num-1) not in nums:
                # this is the start of the subarray
                length=0
                # now considering the num as first,
                # element as we check how many consequetive elements exit:
                while num+length in nums:
                    length+=1
                longest = max(longest, length)
        return longest




#BELOW SOL WORKS, but complexity is O(nlogn), since there is a sorting mechanism
        # nums=sorted(list(set(nums)))
        # print(nums)
        # max_len = 1
        # longest_len = 1
        # if len(nums)==0:
        #     return 0
        # for idx in range(len(nums)-1):
        #     print("compare", nums[idx]+1,nums[idx+1])
        #     if (nums[idx]+1 == nums[idx+1]):
        #         longest_len+=1
        #         max_len = max(max_len, longest_len)
        #         print("max_len", max_len)
        #     else:
        #         longest_len = 1
        # return max_len


