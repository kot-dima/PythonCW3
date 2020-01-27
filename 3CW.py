# from calc import *

# s = 0
# q_index = []

# print("Ready question? GO!")

# print("Enter correct answer 1, 2 or 3")
# print("  ")

# for test in range(0, 12):
#     print(question[test])
#     q_index1 = input("Answear: ")
#     q_index.append(q_index1)
#     if q_index[test] == answear[test]:
#         s += 1

# if s >= 10:
#     print("відмінно - ", s , "балів")
# elif s <= 9 or s >= 7:
#     print("добре - ", s , "балів")
# elif s <= 6 or s >= 4:
#     print("задовільно - ", s , "балів")
# else:
#     print("незадовільно - ", s , "балів")


# -3 (3*1)   -5(5*1)
# -9 (3*3)   -10(5*2)
# -15 (3*5)  -20(5*4)

print("Василина Премудра грала зі Змієм Гориничем у шашки. \nВ цій казці вони з невідомих причин почали їх по черзі їсти...\n Спочатку Василина з’їла у Горинича 3 шашки, а Горинич у Василини – 5 шашок...")

vaseluna = 3
zmiy = 5

v = 3
z = 2

s = []
s1 = []
while True:
    vaselunaN = vaseluna*v
    zmiyN =  zmiy*z
    z += 2
    v += 2
    print(" ")
    print("Василина з'їла ", vaselunaN, "шашок")
    print("Змій Горинич з'їв", zmiyN, "шашок" )
    print(' ')
    s.append(vaseluna)
    s1.append(zmiy)
    theEnd = input("Натисніть Enter для продовження поїдання; \n Введіть \"a\" щоб Змій з'їв Васелину: ")
    if theEnd == "a":
        print("Змій Горинич з'їдає Василину на", len(s), "кроці\n", "Горинич з'їв : ", sum(s), "шашок\n", "Василина:", sum(s1), "шашок")
        break
