low = 0
high =len(nums)-1
mid = int(low+(high-low)/2)
while (low <= high):
     mid = int(low+(high-low)/2)
     if (nums[mid] == target):
         return mid
     if nums[mid] <= nums[high]:
         if target >= nums[mid] and target <=nums[high]:
             low=mid+1
         else:
             high = mid-1
     else:
         if target >= nums[low] and target <=nums[mid]:
             high = mid-1
         else:
             low=mid+1
