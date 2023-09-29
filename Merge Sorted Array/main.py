from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1=nums1[:m]+nums2[:n]
        return nums1
        
nums1 =[1,2,3,0,0,0]
m =3
nums2 =[2,5,6]
n =3


solution = Solution()
obj=solution.merge(nums1, m, nums2, n)
print(obj)
nums3 =[0]
m =1
nums4 =[1]
n =1
obj2=solution.merge(nums3, m, nums4, n)
print(obj2)