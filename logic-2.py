def make_bricks(small, big, goal):
    if goal // 5 <= big and goal % 5 <= small:
        return True
    else:
        return False

print(make_bricks(6, 1, 11))