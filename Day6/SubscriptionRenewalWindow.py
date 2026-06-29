def longestWindow(nums,k):
    left=0
    maxLen=0
    for right in range(len(nums)):
        while nums[right]-nums[left]>k:
            left+=1
        maxLen=max(maxLen,right-left+1)

    return maxLen

nums=[1,3,5,7,9]
k=4
print(longestWindow(nums,k))        