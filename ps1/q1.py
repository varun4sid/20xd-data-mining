import math

#Q1
def getMean(nums):
    if len(nums)>0:
        return sum(nums)/len(nums)
    else:
        return 0


def getMode(nums):
    count = {}
    for i in nums:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    
    maxVal = 0
    for value in count.values():
        if value > maxVal:
            maxVal = value
    
    modes = []
    for key in count.keys():
        if count[key] == maxVal:
            modes.append(key)
            
    return modes


def getMedian(nums):
    nums.sort()
    n = len(nums)
    if n%2 == 0:
        return getMean([nums[int((n/2)-1)],nums[int(n/2)]])
    else:
        return nums[math.floor(n/2)]

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]

    print("Mean : ",getMean(nums))
    print("Median : ",getMedian(nums))
    print("Mode(s) : ",getMode(nums))