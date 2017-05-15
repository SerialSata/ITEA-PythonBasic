# char_10_string = input('input string of min 10 chars: ')
#
# final_str = char_10_string[-3:] + (char_10_string[3:-3])[::-1] + char_10_string[:3]
# print (final_str)

# =======================================

# a = float (input('Сторона А = '))
# b = float (input('Сторона B = '))
# c = float (input('Сторона C = '))
#
# p = (a + b + c) / 2
#
# s = ( p * (p - a) * (p - b) * (p - c) )**0.58
#
# print('Площадь треугольника = ', s)

# =======================================

# a = float(input('Сторона А = '))
# b = float(input('Сторона B = '))
# c = float(input('Сторона C = '))
#
# print(a + b > c and a + c > b and c + b > a)

# =======================================

a = float(input('Сторона А = '))
b = float(input('Сторона B = '))
c = float(input('Сторона C = '))

exist = (a + b > c and a + c > b and c + b > a)

p = (a + b + c) / 2
s = ( p * (p - a) * (p - b) * (p - c) )**0.58

result = s * exist + (-1) * (not exist)

print (result)