class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, c, ans = len(a)-1, len(b)-1, 0, ""
        while i >= 0 or j >= 0 or c:
            c += (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
            ans = str(c % 2) + ans
            c //= 2; i -= 1; j -= 1
        return ans