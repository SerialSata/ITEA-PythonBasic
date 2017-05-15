# a = int(input("a?"))
# b = int(input("b?"))
# c = int(input("c?"))
#
# if (a == b and a > c) or (b == c and c > a) or (a == c and a > b) or a == b == c:
#     print("error")
# elif a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)

# =============================================

# x = 1
# try:
#     a = 5 / x
#     # raise ValueError("AAAAAAA!")
# except ZeroDivisionError:
#     print("Zero")
# except NameError:
#     print("Name")
#     exit()
# # except Exception as e:
# #     print(e)
# else:
#     print("Ok ", a)
# finally:
#     print("the end")
# print("the  end after the end")

# =============================================

# a = b = c = 0
# try:
#     a = float(input("a?"))
# except ValueError:
#     print("Not a number!")
#     exit()
# try:
#     b = float(input("b?"))
# except ValueError:
#     print("Not a number!")
#     exit()
# try:
#     c = float(input("c?"))
# except ValueError:
#     print("Not a number!")
#     exit()
# if a <= 0 or b <= 0 or c <= 0:
#     print("Can't be zero!")
#     exit()
# exist = (a + b <= c and a + c <= b and c + b <= a)
# if exist:
#     print("Impossible triangle!")
#     exit()
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.58
# print("area = ", s)

# =============================================

# номиналы 1 грн, 50 коп, 25 коп, 5 коп, 1 коп

try:
    money = float(input("insert coin: ")) * 100
    if money <= 0:
        raise ValueError("Please, provide positive non-zero value!")
    if money - int(money):
        raise ValueError("Just 2 signs after 0!")
except ValueError as e:
    print (e)
    print("Please! Input right value!")
else:
    leftover = 0
    grn = money // 100
    if grn:
        print("you receive ", grn, " 1 UAH")
    leftover = money - grn*100
    # print(leftover)
    kop_50 = leftover // 50
    if kop_50:
        print("you receive ", kop_50, " 50-kop")
    leftover -= kop_50 *50
    # print(leftover)
    kop_25 = leftover // 25
    if kop_25:
        print("you receive ", kop_25, " 25-kop")
    leftover -= kop_25 * 25
    # print(leftover)
    kop_5 = leftover // 5
    if kop_5:
        print("you receive ", kop_5, " 5-kop")
    leftover -= kop_5 * 5
    if leftover:
        print("you receive ", leftover, " 1-kop")
finally:
    print ("Have a nice day!")
