class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_ = [1]*len(s)
        for i in range(len(s)):
            count1 = count2 = 1
            if i+1<len(s) and s[i] == s[i+1]:
                mid = 1
                count1 = 2
                while i-mid>=0 and i+1+mid<len(s) and s[i-mid] == s[i+1+mid]:
                    count1 += 2
                    mid += 1
            if i-1>=0 and i+1<len(s) and s[i-1] == s[i+1]:
                mid = 1
                count2 = 1
                while i-mid>=0 and i+mid<len(s) and s[i-mid] == s[i+mid]:
                    count2 += 2
                    mid += 1
            list_[i] = max(count1,count2)
        max_ = index = 0
        for j in range(len(list_)):
            if max_ < list_[j]:
                max_ = list_[j]
                index = j
        if max_ % 2 == 0:
            return s[index-max_//2+1:index+1+max_//2]
        else:
            return s[index-(max_+1)//2+1:index+(max_+1)//2]