class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        sort_nums=sorted(nums)
        for i in range(0, len(sort_nums)-2):
            if i>0 and sort_nums[i]==sort_nums[i-1]:
                continue
            target= - sort_nums[i]
            j,k=i+1,len(sort_nums)-1
            while j<k:
                current = sort_nums[j]+sort_nums[k]
                if current==target:
                    ans.append([sort_nums[i], sort_nums[j], sort_nums[k]])
                    j+=1
                    k-=1
                    while j<k and sort_nums[j]==sort_nums[j-1]:
                        j+=1
                elif current<target:
                    j+=1
                else:
                    k-=1

                
        return ans