def count_evens(nums):
    evens = [i for i in nums if i % 2 == 0]
    return len(evens) if evens else 0

def big_diff(nums):
    nums.sort()
    return nums[-1] - nums[0]

def centered_average(nums):
    nums.sort()
    del nums[0]
    del nums[-1]
    return sum(nums)/len(nums)

def sum13(nums):
    if nums:
        if 13 not in nums:
            return sum(nums)
        else:
            indexes = [i for i, x in enumerate(nums) if x == 13]
            for each in indexes:
                if each != len(nums) - 1:
                    nums[each] = 0
                    nums[each+1] = 0
                else:
                    nums[each] = 0
            return sum(nums)
    else:
        return 0


def sum67(nums):
    if not nums:
        return 0
    switch = False
    for i in range(0, len(nums)):
        if switch:
            if nums[i] == 7:
                switch = False
            nums[i] = 0
        if nums[i] == 6:
            switch = True
            nums[i] = 0
    return sum(nums)


def has22(nums):
    return True if '22' in ''.join([str(i) for i in nums]) else False

print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))