Nama = "Raditya Mulya Akbar"
Kelas = "1-A TKJ"
Nim = "42523011"
print("Nama :", Nama)
print("Kelas :", Kelas)
print("Nim :", Nim)
# Exercise 1 (Python Literal)
# Apa tipe-tipe literal dari contoh berikut ini:
# "Hello ", "007"

literal_1 = "Hello "
literal_2 = "007"

# Menampilkan tipe-tipe literal
print("Tipe dari literal 1:", type(literal_1))
print("Tipe dari literal 2:", type(literal_2))

# Exercise 2
# Tipe-tipe literal dari empat contoh berikut:
# "1.5", 2.0, 528, False

literal_1 = "1.5"
literal_2 = 2.0
literal_3 = 528
literal_4 = False

# Menampilkan tipe-tipe literal
print("Tipe dari literal 1:", type(literal_1))
print("Tipe dari literal 2:", type(literal_2))
print("Tipe dari literal 3:", type(literal_3))
print("Tipe dari literal 4:", type(literal_4))

# Exercise 3
# Mengonversi bilangan biner ke desimal
binary_number = "1011"
decimal_value = int(binary_number, 2)
print("Nilai desimal dari", binary_number, "adalah:", decimal_value)

# Exercise 1 (Arithmetic Operators and The Hierarchy of Priorities)
print((2 ** 4), (2 * 4.), (2 * 4))

# Exercise 2
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

# Exercise 3
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

# Exercise 1 (Variables)
var = 2
var = 3
print(var)

# Exercise 2
# Variables yang illegal pada Python ialah : 101, m 101
my_var = 0
m = 1
averylongvariablename = 2
m101 = 3
Del = 4

# Exercise 3
a = '1'
b = "1"
print(a + b)

# Exercise 4
a = 6
b = 3
a /= 2 * b
print(a)

# Exercise 1 (Comments): Output of the following snippet
# print("String #1")
print("String #2")

# Exercise 2: What will happen when you run the following code?
# This is a multiline comment. #
print("Hello!")

# Exercise 1 (The input() function and String Operators): Output of the following snippet
x = int(input("Enter a number: "))  # The user enters 2
print(x * "5")

# Exercise 2: Expected output of the following snippet
x = input("Enter a number: ")  # The user enters 2
print(type(x))

# Exercise 1 (Comparison Oprators and Conditional Executions)
x = 5
y = 10
z = 8

print(x > y)
print(y > z)

# Exercise 2
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

# Exercise 3
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

# Exercise 4
x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

# Exercise 5
x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

# Exercise 6
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

# Exercise 1 (Loop): For loop printing odd numbers from 0 to 10
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Exercise 2: While loop printing odd numbers from 0 to 10
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

# Exercise 3: For loop with a break statement to extract part of an email address
email = "john.smith@pythoninstitute.org"
for ch in email:
    if ch == "@":
        break
    print(ch, end="")

# Exercise 4: For loop with a continue statement to modify a string
digits = "0165031806510"
for digit in digits:
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# Exercise 5: Output of the while loop
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# Exercise 6: Output of the for loop
n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)

# Exercise 7: Output of the for loop
for i in range(0, 6, 3):
    print(i)

# Exercise 1 (Logic and Bit Operation): Logical operators and output
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

# Exercise 2: Bitwise operators and their outputs
x = 4
y = 1

a = x & y  # Bitwise AND
b = x | y  # Bitwise OR
c = ~x     # Bitwise NOT (Complement)
d = x ^ 5  # Bitwise XOR
e = x >> 2 # Bitwise right shift
f = x << 2 # Bitwise left shift

print(a, b, c, d, e, f)


