def first_last6(nums):
  if len(nums) > 1:
    return True if nums[0] == 6 or nums[-1] == 6 else False
  else:
    return True if nums[0] == 6 else False

def same_first_last(nums):
  return True if len(nums) >= 1 and nums[0] == nums[-1] else False

def make_pi():
  return [3,1,4]

def common_end(a, b):
  return True if len(a) >= 1 and len(b) >= 1 and (a[0] == b[0] or a[-1] == b[-1]) else False

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  nums.append(nums.pop(0))
  return nums

def reverse3(nums):
  nums.reverse()
  return nums

def max_end3(nums):
  max = nums[0] if nums[0] > nums[-1] else nums[-1]
  return [max, max, max]

def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) >= 1:
    return nums[0]
  else:
    return 0

def middle_way(a, b):
  c = []
  c.append(a[1])
  c.append(b[1])
  return c
  # return [].__add__([a[1], b[1]])

def make_ends(nums):
  c = []
  c.append(nums[0])
  c.append(nums[-1])
  return c

def has23(nums):
  return True if 2 in nums or 3 in nums else False



