# s = 'ghbdtn'
# print(s)
# s = 'привет'
# print(s)
# b = b'hello'
# print(b, type(b))
# s= 'asdыва.'
# b=s.encode('utf-8')
# print(b)
# print(b.decode("cp1251"))
#
# print("a" > "A")
# print("a" > "b")
# print("11" > "2")
#
# for i in range(32,127):
#     print(chr(i), end =" ")

# ==============================================
#
# import string
# import random
# password = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])
# print(password)

# =============================================

# name = 'Bill'
# age = 23
#
# print( "Name: %s; age: %d" % (name, age))
#
# print( "Name: {}; age: {}".format(name, age))
#
# print( "Name: {}; age: {:>30}".format(name, age))
#
# print( "Name: {1}; age: {0}".format(name, age))

# =============================================

# import re
# s= 'asgfjajhsgf 345-12-67  m,bdvd nm,nm,fnm,d nnmn 325 7623'
# print(re.findall('[0-9]{3}[- ]+[0-9]{2}-?[0-9]{2}', s))

# =============================================
s = 'abba abba'
palindrom = ''
x = 0
window_length = len(s) - x
ss = s[0:window_length]
print(ss[::-1])


if s == ss[::-1]:
    palindrom = ss
    print('1')
    print(palindrom)

for i in range(len(s)):
    print(i)
    ss = s[i:window_length]
    print(ss[::-1])

# ss = s[window_length:window_length:-1]
# while True:
#     if s == ss:
#         palindrom = ss
#         print(palindrom)
#         break
#     else:
#         ss = s[:]
