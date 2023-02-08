#Maximum Average Subarray I
#You are given an integer array nums consisting of n elements, and an integer k.

#Find a contiguous subarray whose length is equal to k that has the maximum average value and
#-return this value. Any answer with a calculation error less than 10^-5 will be accepted.

#My solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        if k == 1:
            return max(nums)
        res = 0
        for i in range(len(nums)):
            place = sum(nums[i : i + k])/k
            if place > res and len(nums[i : i + k]) == k:
                res = sum(nums[i:i+k]) / k
                print(res)
            elif place >= res :
                return(float(res))
        return res
       
# Optimal solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current=0
        for i  in range(k) :
            current+=nums[i]
        maxi = current
        for i in range(k,len(nums)) :
            current+=nums[i]-nums[i-k]
            maxi = max(current,maxi)
        return maxi/k
    

#A pangram is a sentence where every letter of the English alphabet appears at least once.
#Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Optimal solution
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            current_char = chr(ord('a') + i)
            if sentence.find(current_char) == -1:
                return False    
        return True
            
#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#Input: nums = [3,0,1]
#Output: 2
#Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


#Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
#Input: arr = [1,2,3]
#Output: 2
#Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        for number in arr:
            if number + 1 in arr:
                counter += 1
        return counter

#Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1
    #Time Complexity: O(N), where N is the number of elements in the array. In worst case we might end up visiting every element of array twice, once by left pointer and once by right pointer.
    #Space Complexity: O(1). We do not use any extra space.

##Two Sum
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):  
                if nums[i] + nums[j]  == target:
                    return [i, j]
#Running Sum of 1d Array
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        arr.append(nums[0])
        for i in range(len(nums) -1):
            arr.append(arr[i] + nums[i + 1])
        return arr
            
 arr = []
        left = 0
        for i in range(len(nums)):
            if sum(nums[i + left: i+3]) == 0:
                arr.append(nums[i + left : i+3])
            left += 1
        return arr
