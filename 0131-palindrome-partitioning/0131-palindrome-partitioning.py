class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i) -> None:
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j + 1])
                    backtrack(j + 1)
                    part.pop()

        res = []
        part = []
        backtrack(0)
        return res

    def isPalindrome(self, s, i, j) -> bool:
        l,r = i, j
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
        