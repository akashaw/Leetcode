'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here. 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2: return len(s)

        freq = {}
        ans = 0

        for val in s:
            if val not in freq:
                freq[val] = 1
            else:
                freq[val] += 1
        
        for key, val in freq.items():
            if val // 2 > 0:
                ans += 2 * (val // 2)
                freq[key] -= 2 * (val // 2)
        
        for key, val in freq.items():
            if val > 1:
                return 'problem'
            if val == 1:
                ans += 1
                return ans
        
        return ans
