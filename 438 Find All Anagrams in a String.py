'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 
Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s) : return []
        p_dictionary = {}
        s_dictionary = {}
        for indx in range(len(p)):
            p_dictionary[p[indx]] = 1 + p_dictionary.get(p[indx], 0)
            s_dictionary[s[indx]] = 1 + s_dictionary.get(s[indx], 0)
        
        if p_dictionary == s_dictionary:
            res = [0]
        else:
            res = []

        l = 0
        for r in range(len(p) , len(s)):
            s_dictionary[s[r]] = 1 + s_dictionary.get(s[r], 0)
            s_dictionary[s[l]] = -1 + s_dictionary.get(s[l], 0)

            if s_dictionary[s[l]] == 0:
                s_dictionary.pop(s[l])
            l = l + 1
            
            # print(s_dictionary)

            if p_dictionary == s_dictionary:
                res.append(l)

        return res    


'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_l = len(s)
        p_l = len(p)
        p = sorted(p)
        res = []
        for i in range(s_l - p_l + 1):
            if sorted(s[i : i+p_l]) == p:
                res.append(i)
        return res
'''
