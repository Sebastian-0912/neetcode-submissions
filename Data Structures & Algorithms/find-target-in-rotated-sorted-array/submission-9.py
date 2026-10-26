class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        # print(left, right)
        while left<right:
            print(left, right)
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[right]:
                if nums[mid]>target:
                    right=mid-1
                elif nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[mid]<target:
                    left=mid+1
                elif nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
            # print(left, right)
        if nums[left]!=target:
            return -1
        return left