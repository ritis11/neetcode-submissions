class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        pointer = int((l+r)/2)
        while pointer >=0 and pointer<= len(nums) and l<=r:          
            if target == nums[pointer]:
                return pointer
            elif target > nums[pointer]:
                l=pointer+1
            elif target <= nums[pointer]:
                r=pointer-1
            pointer = int((l+r)/2)
        return -1
        