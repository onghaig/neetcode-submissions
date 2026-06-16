class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make 2 sets and then just compare if they are equal.
        if len(s) != len(t):
            return False

        #create an array that will store a count for each letter in strs

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1 #add 1 to the letter we are at in the s string
            count[ord(t[i]) - ord('a')] -= 1 #subtract 1 to the letter we are at in the t string
        for val in count:
            if val != 0: # if the value isn't 0, this means that atleast one of the ch in s != ch in t
                return False
        return True