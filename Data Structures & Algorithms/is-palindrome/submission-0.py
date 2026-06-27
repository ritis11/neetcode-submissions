
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new=''.join(char for char in s if char.isalnum())
        s_new=s_new.lower()
        i,j=(0,len(s_new)-1)
        while i<j:
            if s_new[i]==s_new[j]:
                i+=1
                j-=1
            else:
                return False
        else:
            return True
            

        