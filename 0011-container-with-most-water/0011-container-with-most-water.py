class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        ans = 0
        while l < r:
            width = r - l
            area = min(height[l],height[r]) * width
            ans = max(area, ans)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans
        