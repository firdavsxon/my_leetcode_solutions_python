"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""

def search_triplets(arr):
	arr.sort()
	triplets = []
	for i in range(len(arr)):
		if i>0 and arr[i]== arr[i-1]:
			continue
		search_pair(arr, -arr[i], i+1, triplets)
	return triplets


def search_pair(arr, target_sum, left, triplets):
		right=len(arr)-1
		while left < right:
			current_sum = arr[left]+arr[right]
			if current_sum == target_sum:
				triplets.append([-target_sum, arr[left], arr[right]])
				left+=1
				right-=1
				while left < right and arr[left] == arr[left-1]:
					left += 1
				while left < right and arr[right] == arr[right+1]:
					right -= 1
			elif current_sum > target_sum:
				right -= 1
			elif current_sum < target_sum:
				left+=1






nums = [-5, 2, -1, -2, 3]
nums2= [-3, 0, 1, 1, 1,  2, -1, 1, -2]
# print(search_triplets(nums2))


def search_triplet3(arr):
	triplets = []
	arr.sort()
	for i in range(len(arr)):
		if i > 0 and  arr[i]==arr[-1]:
			continue
		helper(arr, -arr[i], i+1, triplets)
	return triplets

def helper(arr, target_sum, left, triplets):
	right = len(arr)-1
	while left<right:
		current_sum = arr[left] + arr[right]
		if current_sum == target_sum:
			triplets.append([-target_sum, arr[left], arr[right]])
			left +=1
			right -=1
			while left<right and arr[left] == arr[left - 1]:
				left += 1
			while left<right and arr[right] == arr[right +1]:
				right -=1
		elif current_sum < target_sum:
			left += 1
		else:
			right -= 1







array = [-3, 0, 1, 2, -1, 1, -2]
print(search_triplet3(array))

