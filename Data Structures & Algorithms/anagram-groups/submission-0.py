class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        lst_of_lst = []
        for word in strs:
            cnt_lst =[0] * 26
            for char in word:
                cnt_lst[ord(char)-ord('a')]+=1
            value = dict_.get(tuple(cnt_lst), [])
            value.append(word)

            dict_[tuple(cnt_lst)] = value
            print(dict_)
        for key, val in dict_.items():
            lst_of_lst.append(val)
        return lst_of_lst
        