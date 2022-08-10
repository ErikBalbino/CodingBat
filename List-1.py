#first_last6
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
#
#first_last6([1, 2, 6]) → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
  return True if (nums[0]==6 or nums[-1]==6) else False

#same_first_last
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
#
#same_first_last([1, 2, 3]) → False
#same_first_last([1, 2, 3, 1]) → True
#same_first_last([1, 2, 1]) → True

def same_first_last(nums):
    return (len(nums)>0 and nums[0]==nums[-1])

#make_pi
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
#
#make_pi() → [3, 1, 4]
def make_pi():
    return [3, 1, 4]

#common_end
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

#common_end([1, 2, 3], [7, 3]) → True
#common_end([1, 2, 3], [7, 3, 2]) → False
#common_end([1, 2, 3], [1, 3]) → True
def common_end(a, b):
  return (a[0]==b[0] or a[-1]==b[-1])
