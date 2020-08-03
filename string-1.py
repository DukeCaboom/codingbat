def hello_name(name):
    return "Hello " + name + "!"

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

def make_out_word(out, word):
    return out[0:2] + word + out[2:]
    
def extra_end(str):
    return str[-2:] * 3

def first_two(str):
    if len(str) > 2:
        return str[0:2]
    else:
        return str

def first_half(str):
    return str[0:len(str)/2]

def without_end(str):
  if len(str) > 2:
    return str[1:-1]
  else:
    return ""


def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  if len(str) > 2:
    return str[2:] + str[0:2]
  else:
    return str

print(make_tags('i', 'yay'))