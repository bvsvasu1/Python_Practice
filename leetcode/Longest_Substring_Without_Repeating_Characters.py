#SOLUTION ONE:
# RUNTIME
# 1287ms Beats 5.00%
# Memory
# 16.87 MB Beats 13.34%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        s_lst = list(s)
        j=0
        k=1
        tmp_lst = []
        tmp_lst.append(s_lst[j])
        max_lst = []
        while k<len(s_lst):
            #print(s_lst,j,k)
            if (s_lst[j]!=s_lst[k] and s_lst[k] not in tmp_lst):
                tmp_lst.append(s_lst[k])
                k+=1
            else:
                j+=1
                if len(max_lst)<len(tmp_lst):
                    max_lst=tmp_lst
                tmp_lst = []
                tmp_lst.append(s_lst[j])
                k=j+1
        if len(max_lst)<len(tmp_lst):
            max_lst=tmp_lst
        return len(max_lst)
        

        