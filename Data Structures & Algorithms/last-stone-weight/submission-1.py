class Solution:
    def lastStoneWeight(self, stones) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            ele1=heapq.heappop_max(stones)
            ele2=heapq.heappop_max(stones)
            print(ele1, ele2)
            if (ele1!=ele2):
                ele3= abs(ele1-ele2)
                heapq.heappush_max(stones, ele3)
        ans = stones[0] if len(stones)>0 else 0
        return ans


sol = Solution()
sol.lastStoneWeight([10,4,2,10])