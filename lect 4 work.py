# import random
#
# MAX_TRIES = 5
# secret = random.randint(1, 10)
# tries = 0
# # is_guessed = False
#
# while tries < MAX_TRIES:
#     try:
#         guess = int(input('You have 5 tries. Guess a number: '))
#     except ValueError:
#         print("Please, provide a number between 1 and 10")
#         continue
#     tries += 1
#     if secret == guess:
#         print("You're right! Congratulations!")
#         # is_guessed = True
#         break
#     if secret < guess:
#         print("Little less")
#     else:
#         print("Little more")
# else:
#     print('You are looser!')
# # if not is_guessed:
# #     print ('You are looser!')

# ===================================================

# import random
#
# min_limit = 1
# max_limit = 10
# MAX_TRIES = 5
# tries = 0
#
# print("I want to guess a number between 1 and 10, let's try!")
# while tries < MAX_TRIES:
#     tries += 1
#     random_guess = random.randint(min_limit, max_limit)
#     print(random_guess)
#     guess = input("Am i right? Input 'yes', '>' or '<'")
#     if guess == 'yes':
#         print('Woohoo! I win!')
#         break
#     elif guess == '<':
#         max_limit = random_guess
#     elif guess == '>':
#         min_limit = random_guess
#     else:
#         print("i didn't understand!")
#         guess = input("Am i right? Input '>' or '<'")
# else:
#     print("Too bad :( But ok, let's try one more time!")

# ===================================================

# import copy
# l = [1,2,[1,2,3]]
# l1 = l[:]
# l1 = list(l)
# l1 = copy.deepcopy(l)
# print(list(range(10)))
# print(list(range(2,10,2)))

# ===================================================

# for i in range(100000):
#     if i*i >=50:
#         break
#     print(i, i*i)


# for index, value in enumerate("hello"[3:8], 2): #2 - Начало нумерации
#     print(index, value)


# L = [1,2,3,4,5]
# x=input()
# for i in L:
#     if i == x:
#         print ('yes')
#         break
#     else:
#         print ('no')

# L = [x*x for x in range(10) if x%2]
# print (L)

# ===================================================

'''
ДЗ
1. сделать автомат с разменом монет на циклах
2. найти произведение элементов списка, минимальный и максимальный элемент списка
3. найти 2 одинаковых элемента в списке
4. поменять местами мин и макс элементы списка
5. Сдвиг на 1 элемент в списке, циклический сдвиг

'''

import random

L = []
for i in range(10):
    L.append(random.randint(1, 100))
print('List: ', L)

print("========= Composition of all list members =========")
composition = 1
for i in L:
    composition *= i
print('Composition: ', composition)

print("========= Find min & max =========")
min_elem = max_elem = L[0]
iterator = min_place = max_place = 0
for i in L:
    if i < min_elem:
        min_elem = i
        min_place = iterator
    if i > max_elem:
        max_elem = i
        max_place = iterator
    iterator += 1
print('Min element: ', min_elem, '; Max element: ', max_elem)

print("========= Сhange places in list for min max elements =========")
L[min_place] = max_elem
L[max_place] = min_elem
print(L)

print("========= Move for 1 list element to left =========")
for i in range(len(L)):
    if i == 0:
        continue
    else:
        L[i - 1] = L[i]
L.pop(len(L) - 1)
print(L)

print("========= Cycling all list members =========")
CYCLE_COUNT = int(input("Input needed cycles count: "))
z = 0
print('Initial list: ', L)
while z < CYCLE_COUNT:
    first_elem = L[0]
    for i in range(len(L)):
        if i == 0:
            continue
        else:
            L[i - 1] = L[i]
    L.pop(len(L) - 1)
    L.append(first_elem)
    print(L)
    z += 1
