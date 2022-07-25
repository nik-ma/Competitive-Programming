class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        newarray=[0]*(n+m)
        i=n-1
        j=m-1
        k=n+m-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                newarray[k]=nums1[i]
                i-=1
            else:
                newarray[k]=nums2[j]
                j-=1
            k-=1
        while i>=0:
            newarray[k]=nums1[i]
            i-=1
            k-=1
        while j>=0:
            newarray[k]=nums2[j]
            j-=1
            k-=1
        # print(newarray)
        if (n+m)%2:
            return (newarray[(n+m)//2])
        return (newarray[(n+m)//2]+newarray[(n+m)//2-1])/2
            