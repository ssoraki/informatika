import math


def task1():
    x = float(input("введите х\n"))
    y = float(input("введите y\n"))
    z = float(input("введите z\n"))

    a1 = (abs(x - 1)) ** (1 / 5)
    a2 = a1 + math.exp(-y)
    a3 = math.sin(x) + math.log10(1 + y)
    a = a2 / a3
    print("a = ", "{:.4}".format(a) + "\n")

    b1 = (abs(z + 71)) ** (1 / 5)
    b2 = math.sin(b1)
    b3 = (abs(y)) ** (1 / 3)
    b4 = math.cos(b3)
    b = b2 + b4 + (x ** (1 / 3)) + (y ** (1 / 4))
    print("b = ", "{:.4}".format(b))


def task2():
    a = float(input("введите а\n"))
    x = float(input("введите x\n"))
    b = -1
    c = 2

    f = ((x + a) ** (1 / 2)) + ((x ** 2 + b) / x)
    print("f(x) = ", "{:.4}".format(f))


def task3():
    x = float(input("введите x\n"))
    f1 = math.sin(math.cos(x))
    f2 = math.log(x + 1)
    f = f1 / f2
    print("f(x) = ", "{:.4}".format(f))


def task4():
    a = float(input("введите а\n"))
    b = float(input("введите b\n"))
    c = float(input("введите c\n"))
    summ = 4 * (((a ** 2) * (b ** 2) * (c ** 2)) ** (1/2))
    print("sum = ", "{:.4}".format(summ))


def task5():
    h = float(input("введите h\n"))
    v = float(input("введите v\n"))
    g = 9.8066
    vk = (v ** 2 + 2 * g * h) ** (1 / 2)
    t = (vk - v) / 2
    print("t = ", "{:.4}".format(t))


def task6():
    alpha = float(input("введите alpha в градусах\n"))
    beta = float(input("введите beta в градусах\n"))
    k = float(input("введите сторону k\n"))
    a = (k * math.sin(math.radians(alpha))) / math.sin(math.radians(beta))
    s = 0.5 * k * a * math.sin(math.radians(180 - (alpha + beta)))
    print("s = ", "{:.4}".format(s))
 

def task7():
    A = float(input("введите A\n"))
    B = float(input("введите B\n"))
    C = float(input("введите C\n"))
    if not (A >= -10 and A <= 10 and A != 0 and 
              B >= -10 and B <= 10 and 
              C >= -10 and C <= 10): 
        print("Введены некоректные данные\n")
    else:
        D = B ** 2 - 4 * A * C
        if (D < 0):
            print("D < 0")
            exit(0)
        x1 = (-B + D ** (1/2)) / (2 * A)
        x2 = (-B - D ** (1/2)) / (2 * A)
        if (x1 >= x2):
            print("x1 = ", "{:.4}".format(x2) + "\n")
            print("x2 = ", "{:.4}".format(x1) + "\n")
        else:
            print("x1 = ", "{:.4}".format(x1) + "\n")
            print("x2 = ", "{:.4}".format(x2) + "\n")


def task8():
    m = float(input("Введите массу тела\n"))
    s = float(input("Введите путь до остановки\n"))
    t = float(input("Введите время до полной остановки (в секундах)\n"))
    sv = float(input("Введите начальную скорость (в м/с)\n"))
    a = sv / t
    f = m * a 
    print("Сила трения, действующая на тело = ", "{:.4}".format(f))


def task9():
    credit = float(input("введите сумму кредита\n"))
    rate = float(input("введите ставку кредита в % годовых\n"))
    summ = (credit / 100 * rate)
    print("Сумма начисленных процентов = ", "{:.4}".format(summ))


try:
    task3()
except ZeroDivisionError:
    print("делить на ноль нельзя")
    exit(0)
except ValueError:
    print("логарифм <= 0")
    exit(0)
