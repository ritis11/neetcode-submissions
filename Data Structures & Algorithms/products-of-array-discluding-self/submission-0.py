class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            i = 0
            j = len(nums)-1
            ans = []
            arr_forward = {-1:1}
            initial = 1
            backward = 1
            arr_back = {j+1:1}

            while i < len(nums) and j>0:
                initial = initial * nums[i]
                arr_forward[i] = initial
                backward = backward * nums[j]
                arr_back[j] = backward
                i+=1
                j-=1
            for k in range(len(nums)):
                ans.append(arr_forward.get(k-1)*arr_back.get(k+1))
            return ans
