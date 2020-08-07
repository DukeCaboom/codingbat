def double_char(str):
    double_st = ''
    for each in str:
        double_st += each * 2
    return double_st

def count_hi(str):
    return str.count('hi')

def cat_dog(str):
    return True if str.count('cat') == str.count('dog') else False

def count_code(str):
    counter = str.count('code')
    new_str = str.replace('code', '')
    if len(new_str) >=4:
        for i in range(len(new_str)-3):
            if new_str[i] == 'c' and new_str[i+1] == 'o' and new_str[i+3] == 'e':
                counter += 1
    return counter

def end_other(a, b):
    if len(a) > len(b):
        return True if a[::-1][0:len(b)][::-1].lower().lower() == b.lower() else False
    elif len(a) < len(b):
        return True if b[::-1][0:len(a)][::-1].lower() == a.lower() else False
    else:
        return True if a.lower() == b.lower() else False

def xyz_there(str):
    if str.count('xyz') < 1:
        return False 
    elif str.count('xyz') >= 1:
        while str.count('xyz') != 0:
            print(f"str: {str}")
            if str.find('xyz') == 0 or str[str.find('xyz') - 1] != '.':
               return True
            str = str.replace(str[str.find('xyz') - 1], '', 1)
            str = str.replace('xyz', '', 1)
    return False

print(xyz_there('1.xyz.xyz2.xyz'))