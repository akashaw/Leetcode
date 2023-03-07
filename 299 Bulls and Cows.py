'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 
Constraints:

1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
'''

# https://leetcode.com/problems/bulls-and-cows/solutions/839444/python-simple-solution-with-counters-explained/
# Let us first evaluate number of bulls B: by definition it is number of places with the same digit in secret and guess: so let us just traverse our strings and count it.
# Now, let us evaluate both number of cows and bulls: B_C: we need to count each digit in secret and in guess and choose the smallest of these two numbers. Evaluate sum for each digit.
# Finally, number of cows will be B_C - B, so we just return return the answer!

class Solution:
    def getHint(self, secret, guess):
        B = sum([x==y for x,y in zip(secret, guess)])
		Count_sec = Counter(secret)
        Count_gue = Counter(guess)
        B_C = sum([min(Count_sec[elem], Count_gue[elem]) for elem in Count_sec])
        return str(B) + "A" + str(B_C-B) + "B"

