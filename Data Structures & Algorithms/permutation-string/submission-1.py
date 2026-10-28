class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=len(s1)-1
        i, j = 0, l
        initial_subsring = s2[0:len(s1)]
        dict_s1 = {}
        dict_s2 = {}
        for ele in initial_subsring:
            dict_s2[ele] = dict_s2.get(ele, 0) + 1
        for ele in s1:
            dict_s1[ele] = dict_s1.get(ele, 0) + 1

        while j<len(s2):
            if dict_s2 == dict_s1:
                return True
            else:
                j+=1
                if j>=len(s2):
                    return False
                dict_s2[s2[j]] = dict_s2.get(s2[j], 0) + 1

                dict_s2[s2[i]] = dict_s2.get(s2[i], 0) - 1

                if dict_s2[s2[i]] <= 0:
                    dict_s2.pop(s2[i])

                i+=1
        return False



        