class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9 ]+', '', s).split(\ \)
        s = \\.join(s).lower()
        
        l, r = 0, len(s) - 1

        while l < r:
            if s[r] != s[l] : return False
            l += 1
            r -= 1
        
        return True