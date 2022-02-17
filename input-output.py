# 2.3 Custom Separator (Step 6)
x = input()
print(input(), input(), input(), sep = x)


# 2.4 Three consecutive numbers (Step 5)
a = int(input())
print(a, a + 1, a + 2, sep="\n")


# 2.5 Compartment number (Step 10)
n = int(input())
x = -n // 4
print(-x)


# 2.5 Recalculating the time interval (Step 11)
n = int(input())
print(n, 'min is', n // 60, 'hour', n % 60, 'min.')


# 2.5 Permutation of digits (Step 14)
n = int(input())
c = n % 10
b = (n % 100) // 10
a = n // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')


# 2.5 A four-digit number (Step 15)
n = int(input())
a = n % 10
b = (n % 100) // 10
c = (n % 1000) // 100
d = n // 1000
print('The figure in the thousands position is equal to', d)
print('The number in the hundreds position is equal to', c)
print('The digit in the tens position is equal to', b)
print('The digit in the position of units is equal to', a)


# 3.2 Step 4
n = int(input())
nn = n * 10 + n
nnn = n * 110 + n
print(n + nn + nnn)
