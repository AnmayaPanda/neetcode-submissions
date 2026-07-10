class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalpha() == True or char.isnumeric() == True)
        s = s.lower()

        def isPalindrome(s):
            return s == "".join(s[i] for i in range(len(s)) if s[i] == s[-i-1])

        return isPalindrome(s)