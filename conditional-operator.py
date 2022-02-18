# 4.1 Password (Step 4) - interesting solution
print('Password accept' if input() == input() else 'Password is not accept')


# 4.1 Ratio (Step 6)
number = int(input())
a = number % 10
b = (number % 100) // 10
c = (number % 1000) // 100
d = number // 1000
if d + a == c - b:
    print('YES')
else:
    print('NO')


# 4.1 The smallest of the four numbers (Step 10)
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)


#  4.1 Only+ (Step 12)
a = int(input())
b = int(input())
c = int(input())
if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0
print( a + b + c)


# 4.2 Leap year (Step 13)
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')


# 4.2 Rook's Move (Step 14)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y2 == y1:
    print("YES")
else:
    print("NO")


# 4.2 King's Move (Step 15)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x2 == x1 or x2 == x1 + 1 or x2 == x1 - 1) and (y2 == y1 or y2 == y1 + 1 or y2 == y1 -1):
    print('YES')
else:
    print('NO')


# 4.3 Intersection of segments (Step 11)
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('empty set')
else:
    if a1 > a2:
        a2 = a1
    if b1 > b2:
        b1 = b2
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)
# simplified the condition of the intersection of two segments to the limit:
# 1. if they do not intersect at all - the first IF;
# 2 if they intersect - then we have 4 IFs below;
# so, we need the second and third.


# 5.1 The beginning of the century (Step 1)
year = int(input())
if year % 10 == 0 and (year % 100) // 10 == 0:
    print('YES')
else:
    print('NO')


# 5.1 Chess board (Step 2)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')


# 5.1 Bishop's Move (Step 6)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')


# 5.1 Knight's Move (Step 7)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print ('YES')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print ('YES')
else:
    print ('NO')


# 5.1 Queen's Move (Step 8)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
