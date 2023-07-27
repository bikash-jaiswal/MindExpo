## [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

#### First approach
> Approach : 
> 1. Traverse through nums2 and append its elements to the end of nums1 starting from index m.
> 2. Sort the entire nums1 array using sort() function

## Solution

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left:int = 0
        right:int = 0

        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                left += 1
            else:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                

        right = 0
        while left < m+n and right < n:
            nums1[left] = nums2[right]
            right += 1
            left += 1

        return nums1.sort()  
```
## Time Complexity
> 0(N +0M) + 0((m+n)log(m+n))
## space complexity
> 0(1)

Question: Can we remove the sorting function?

## Approach 2: 
> Since both array are sorted, 
> first iteration: Start looking from back, compare and reverse
> nums2[] will have all larger value and nums1[] will have smaller 

```python
```

## Time Complexity
> 0(N + M)
## space complexity
> 0(1)