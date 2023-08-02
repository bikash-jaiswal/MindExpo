## [27. Remove Element](https://leetcode.com/problems/remove-element/   /)

#### First approach
> Approach : 
> 1. use two ptr technique, 
> 2. left = 0, right = len[]-1
> 3. return left 

## Solution

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:    
                left += 1
        return left


```
## Time Complexity
> 0(n)
## space complexity
> 0(1)
