class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            # if count_dict.get(num) is None:
            #     count_dict[num] = 1
            # else:
            #     count_dict[num]+=1
        count_lst = sorted(list(count_dict.values()))
        top_k = count_lst[-k:]
        # print("top_k:", top_k, "count_dict:", count_dict, "count_lst:", count_lst)
        return [key for key, val in count_dict.items() if val in top_k]
        