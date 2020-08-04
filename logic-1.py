def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    elif cigars >= 40 and cigars <= 60:
        return True
    else:
        return False

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    if is_summer and temp >= 60 and temp <= 100:
        return True
    elif temp >= 60 and temp <= 90:
        return True
    else:
        return False


def caught_speeding(speed, is_birthday):
    token = 5 if is_birthday else 0
    if speed <= 60 + token:
        return 0
    if speed >= 61 + token and speed <= 80 + token:
        return 1
    if speed >= 81 + token:
        return 2

def sorta_sum(a, b):
    sum_r = a + b
    if sum_r >= 10 and sum_r <= 19:
        return 20
    else:
        return sum_r

def alarm_clock(day, vacation):
    weekday = [1,2,3,4,5]
    if vacation:
        return "10:00" if day in weekday else "off"
    else:
        return "7:00" if day in weekday else "10:00"

def love6(a, b):
    return True if (a == 6 or b == 6) or a + b == 6 or abs(a - b) == 6 else False

def in1to10(n, outside_mode):
    return True if ( n >= 1 and n <= 10 and not outside_mode ) or (outside_mode and (n <= 1 or n >= 10) ) else False

def near_ten(num):
    return True if num % 10 in [0, 1, 2 , 8, 9] else False