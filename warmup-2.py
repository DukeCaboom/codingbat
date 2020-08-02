def string_times(str, n):
  return n * str


def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[0:3] * n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  r = ''
  while str:
    r += str[::-1]
    if len(str) != 1:
      str = str[0:len(str)-1]
    else:
      str = ''
  return r[::-1]


def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  count = 0
  for i in range(0, len(str)-2):
    if str[i:i+2] == last2:
      count += 1

  return count


def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  return count


def array_front9(nums):
  if len(nums) < 4:
    return True if 9 in nums else False
  else:
    return True if 9 in nums[0:4] else False

def array123(nums):
  print(str(nums))
  return True if '123' in ''.join(str(i) for i in nums) else False

def string_match(a, b):
  counter = 0
  for_list = a if len(a) < len(b) else b
  for i in range(len(for_list)-1):
    if a[i:i+2] == b[i:i+2]:
      counter += 1

  return counter



print(string_match('abc', 'abc'))


