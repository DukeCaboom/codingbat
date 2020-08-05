def make_bricks(small, big, goal):
    if goal // 5 <= big and goal % 5 <= small:
        return True
    elif big * 5 <= goal and abs(( big * 5 ) - goal) <= small:
        return True
    elif big * 5 >= goal and abs( small - goal ) // 5 <= big and abs( small - goal ) % 5 == 0:
        return True
    else:
        return False
  
def lone_sum(a, b, c):
    if a != b and b != c and a != c:
        return a + b + c
    elif a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b == c and b != a:
        return a
    else:
        return 0

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c

def no_teen_sum(a, b, c):
    teens = [i for i in range(13, 20)]
    teens.remove(15)
    teens.remove(16)
    sum1 = 0
    if a not in teens:
        sum1 += a
    if b not in teens:
        sum1 += b
    if c not in teens:
        sum1 += c
    return sum1        
  

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if int(str(num)[-1]) < 5:
        return abs(num - (num % 5))
    else:
        return abs(num - (num % 5)) + 5


def close_far(a, b, c):
    if is_close(a, b):
        if is_far(a, c):
            return True
        else:
            return False
    elif is_close(a, c):
        return True
    else:
        return False

def is_close(x1, x2):
    if abs(x1 - x2) <= 1:
        return True
    else:
        return False

def is_far(x1, x2):
    if abs(x1 - x2) >= 2:
        return True
    else:
        return False




print(make_bricks(6, 1, 11))