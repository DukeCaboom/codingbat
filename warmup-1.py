def sleep_in(weekday, vacation):
    return True if not weekday or vacation else False

def monkey_trouble(a_smile, b_smile):
    return True if (a_smile and b_smile) or (not a_smile and not b_smile) else False

def sum_double(a, b):
    return a + b if a != b else 2 * (a + b)

def diff21(n):
    return abs(21 - n) if n <= 21 else 2 * abs(21 - n)

def parrot_trouble(talking, hour):
    return True if talking and (hour < 7 or hour > 20) else False

def makes10(a, b):
    return True if (a + b == 10) or a == 10 or b == 10 else False

def near_hundred(n):
    return True if ( n <= 110 and n >= 90 ) or ( n <= 210 and n >= 190 ) else False

def pos_neg(a, b, negative):
    if negative:
        return True if a < 0 and b < 0 else False
    else:
        return True if ( (a < 0 and b > 0) or (a > 0 and b < 0) ) else False

def not_string(word):
    return 'not ' + word if word[0:3] != 'not' else word

def missing_char(str, n):
    return str[0:n] + str[n+1:]

def front_back(str):
    if len(str) <= 1:
        return str
    elif len(str) == 2:
        return str[::-1]
    else:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]

def front3(str):
    if len(str) < 3:
        return 3*str
    else:
        return 3*str[0:3]

print(front3('java'))