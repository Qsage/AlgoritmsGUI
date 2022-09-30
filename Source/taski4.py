def Task1():
    name = input()
    print('Hello,', name + '!')


# print(Task1())


def Task2():
    pingvin = int(input())
    x = ('    _~_    ' * pingvin)
    y = ('   (o o)   ' * pingvin)
    z = ('  /  V  \  ' * pingvin)
    b = (' /(  _  )\ ' * pingvin)
    f = ('   ^^ ^^   ' * pingvin)
    print(x)
    print(y)
    print(z)
    print(b)
    print(f)


# print(Task2())


def Task3():
    n = int(input())
    k = int(input())
    print(k // n)


# print(Task3())


def Task4():
    n = int(input())
    k = int(input())
    print(k % n)


# print(Task4())


def Task5():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    t = (b + d) // 100
    x = (b + d) % 100
    print(a + c + t, '', x)


# print(Task5())

def Task6():
    n = int(input())
    print(2 ** n)


# print (Task6())

def Task7():
    n = int(input())
    print(n % 10)


# print(Task7())

def Task8():
    n = int(input())
    print(n // 10)


# print(Task8())
def Task9():
    n = int(input())
    x = n // 10
    print(x % 10)


# print(Task9())
def Task10():
    n = int(input())
    x = n % 10
    c = n // 100
    h = int(((n - x) / 10) % 10)
    print(x + c + h)


# print(Task10())
def Task11():
    print('A' * 100)


# print (Task11())
def Task12():
    n = int(input())
    x = n // 60
    h = n % 60
    print(x, '', h)


# print (Task12())
def Task13():
    a = int(input())
    b = int(input())
    n = int(input())
    y = b * n % 100
    i = b * n // 100
    x = a * n + i
    print(x, '', y)


# print(Task13())

def Task14():
    n = int(input())
    print('The next number for the number', n, 'is', n + 1)
    print('The previous number for the number', n, 'is', n - 1)


# print(Task14())
def Task15():
    n = int(input())
    print((n - 1) ** 2)


# print (Task15())
def Task16():
    n = int(input())
    print((n + 2) - (n % 2))


# print(Task16())
def Task17():
    n = input()
    print(n * 100)
    x = int(n * 100)
    print(x ** 2)


# print(Task17())
def Task18():
    v = int(input())
    t = int(input())
    print((v * t) % 109)


# print(Task18())
def Task19():
    x = int(input())
    z = int(input())
    v = int(input())
    o = int(input())
    y = int(input())
    t = int(input())
    x = x * 3600
    o = o * 3600
    z = z * 60
    y = y * 60
    b = x + z + v
    a = o + y + t
    print(a - b)


# print(Task19())
def Task20():
    n = int(input())
    m = int(input())
    print((m - 1 + n) // n)


# print(Task20())
def Task21():
    n = int(input())
    x = n // 1000
    print(x)
    p = n % 1000 // 100
    print(p)
    b = n % 1000 % 100 // 10
    print(b)
    c = n % 10
    print(c)
    aboba = x - c
    print(aboba)
    aboba2 = p - b
    print(aboba2)
    print(aboba + aboba2 + 1)


# print(Task21())
def Task31():
    a = int(input())
    b = int(input())
    if a > b:
        print(a)
    else:
        print(b)


# print(Task31())
def Task32():
    a = int(input())
    b = int(input())
    if a > b:
        print(1)
    elif a < b:
        print(2)
    else:
        print(0)


# print(Task32())
def Task33():
    a = int(input())
    b = int(input())
    c = int(input())
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


# print(Task33())
def Task34():
    a = int(input())
    if a % 4 == 0 and a % 100 != 0:
        print('YES')
    else:
        if a % 400 == 0:
            print('YES')
        else:
            print('NO')


# print(Task34())
def Task35():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if c - a <= 1 and c - a > -2 and d - b <= 1 and d - b > -2:
        print('YES')
    elif c - a >= -1 and c - a < 2 and d - b >= -1 and d - b < 2:
        print('YES')
    else:
        print('NO')


# print(Task35())
def Task36():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if (a + b) % 2 == 0 and (c + d) % 2 == 0:
        print('YES')
    else:
        print('NO')


# print(Task36())
def Task37():
    n = int(input())
    m = int(input())
    k = int(input())
    if k % m == 0 and k <= m * n:
        print('YES')
    else:
        print('NO')


# print(Task37())
def Task38():
    n = int(input())
    if n > 10 and n < 15:
        print(str(n), 'korov')
    else:
        if n % 10 == 1:
            print(str(n) + ' korova')
        elif n % 10 > 1 and n % 10 < 5:
            print(str(n) + ' korovy')
        else:
            print(str(n) + ' korov')


# print(Task38())
def Task39():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
        print('YES')
    elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
        print('YES')
    elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
        print('YES')
    elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
        print('YES')
    else:
        print('NO')


# print(Task39())
def Task310():
    a = int(input())
    b = int(input())
    c = int(input())
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        if a + b <= c or b + c <= a or c + a <= b:
            print('impossible')
        else:
            print('rectengular')
    elif (a ** 2 + b ** 2) > c ** 2 or (a ** 2 + c ** 2) > b ** 2 or (b ** 2 + c ** 2) > a ** 2:
        if a + b <= c or b + c <= a or c + a <= b:
            print('impossible')
        else:
            print('acute')
    elif (a ** 2 + b ** 2) < c ** 2 or (a ** 2 + c ** 2) < b ** 2 or (b ** 2 + c ** 2) < a ** 2:
        if a + b <= c or b + c <= a or c + a <= b:
            print('impossible')
        else:
            print('obtuse')
    else:
        print('impossible')


# print(Task310())
def Task311():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0) and (a % 2 != 0 or b % 2 != 0 or c % 2 != 0):
        print('YES')
    else:
        print('NO')


# print(Task311())
def Task312():
    a, b, c = int(input()), int(input()), int(input())
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    print(a, b, c)


# print(Task312())
def Task313():
    a, b, c = int(input()), int(input()), int(input())
    if a == b and a == c:
        print('3')
    elif (a == b and a != c) or (a != b and b == c) or (a == c and b != c):
        print('2')
    else:
        print('0')


# print(Task313())
def Task314():
    k = int(input())
    if (k % 10 + k // 10) % 3 == 0 or k % 5 == 0:
        print('YES')
    else:
        print('NO')


# print(Task314())
def Task315():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    x1 = -(b / a)
    x2 = -(d / c)
    if x1 != x2:
        print(x1)
    elif x1 == x2 or x2 == 0:
        print('NO')
    elif a == 0 and b == 0:
        print('INF')


# print(Task315())


def Task41():
    n = int(input())
    i = 1
    while (i ** 2) <= n:
        print(i ** 2)
        i += 1


# print(Task41())

def Task42():
    n = int(input())
    i = 2
    while n % i != 0:
        i += 1
    print(i)

#print(Task42())
def Task43():
    n = int(input())
    i = 2
    p = 1
    while i * p <= n * 2:
        print(i * p // 2)
        p *= 2


# print(Task43())
# def Task44():
#     n = int(input())
#     n1 = 0
#     if n == 1:
#         print('YES')
#     else:
#         while n >= 1:
#             if n1 >=0:
#                 n1 += n / 2
#             if n1 == 1:
#                 print('YES')
#             else:
#                 print('NO')
# print(Task44())
def Task44():
    n = int(input())
    if n == 1:
        print('YES')
    while n >= 1:
        if n != 1:
            n = n / 2
        elif n == 1:
            print('YES')
            break
    if n < 1:
        print('NO')


# print(Task44())
def Task45():
    x = int(input())
    y = int(input())
    d = 1
    while x < y:
        x += x * 10 / 100
        d += 1
    print(d)


# print(Task45())
def Task46():
    x = 1
    z = 0
    while x != 0:
        x = int(input())
        if z < x:
            z = x
    print(z)


# print(Task46())

def Task47():
    x = int(input())
    i = 1
    sum = 0
    while i <= x:
        sum += i ** 2
        i += 1
    print(sum)
#print(Task47())
def Task48():
    x = 1
    z = 0
    while x !=0:
        x = int(input())
        z += 1
    print(z)

#print(Task48())
def Task49():
    x = 1
    z = 0
    while x !=0:
        x = int(input())
        z += x
    print(z)
#print(Task49())
def Task410():
    x = 1
    z = 0
    count = -1
    while x !=0:
        x = int(input())
        z += x
        count +=1
    print(z/count)
#print(Task410())
def Task411():
    x = 1
    z = -1
    while x !=0:
        x = int(input())
        if x % 2 == 0:
            z +=1
        else:
            continue
    print(z)
#print(Task411())
def Task412():
    x = 1
    z = 0
    count = 0
    while x !=0:
        x = int(input())
        if x > z:
            z, count = x, 1
        elif x == z:
            count += 1


    print(count)
print(Task412())
