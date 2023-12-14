Nama = "Raditya Mulya Akbar"
Kelas = "1-A TKJ"
Nim = "42523011"
print("Nama :", Nama)
print("Kelas :", Kelas)
print("Nim :", Nim)

print("Python Literal")
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

print("Variables")
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

print("Comments")
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

print("Comparison Operators and Conditional Execution")
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


print("Loop")
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

print("Logic and Bit Operation")
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

print("List")
# Exercise 1 (List)
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

# Exercise 2
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

# Exercise 3
lst = []
del lst
# print(lst)  # Uncomment this line to see the NameError
print("Jika ingin melihat NameError yang bagian printnya di uncomment dulu")

# Exercise 4
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

print("Sorting Simple lists")
# Exercise 1 (Sorting Simple lists)
lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

# Exercise 2
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()
print(lst)

# Exercise 3
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()
print(lst)

print("List Processing")
# Exercise 1 (List Processing)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)  # Output: ['B', 'C']

# Exercise 2
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)  # Output: ['B', 'C']

# Exercise 3
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)  # Output: []

# Exercise 4
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)  # Output: ['A', 'B', 'C']

# Exercise 5
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)       # outputs True
print("A" in my_list)     # outputs True
print(3 not in my_list)   # outputs True
print(False in my_list)   # outputs False

print("Array Multidimensional")

# Array 2D untuk menyimpan nilai siswa (3 siswa, 3 mata pelajaran)
nilai_siswa = [
    [75, 80, 85],  # Nilai siswa 1: Matematika, Bahasa Inggris, IPA
    [60, 70, 75],  # Nilai siswa 2: Matematika, Bahasa Inggris, IPA
    [90, 85, 95]   # Nilai siswa 3: Matematika, Bahasa Inggris, IPA
]

# Menampilkan nilai setiap siswa pada setiap mata pelajaran
for i, nilai in enumerate(nilai_siswa, start=1):
    print(f"Nilai Siswa {i}: {nilai}")

# Menghitung rata-rata nilai setiap siswa
for i, nilai in enumerate(nilai_siswa, start=1):
    rata_rata = sum(nilai) / len(nilai)
    print(f"Rata-rata nilai Siswa {i}: {rata_rata:.2f}")

# Menghitung rata-rata nilai setiap mata pelajaran
nilai_matematika = [siswa[0] for siswa in nilai_siswa]
nilai_inggris = [siswa[1] for siswa in nilai_siswa]
nilai_ipa = [siswa[2] for siswa in nilai_siswa]

rata_matematika = sum(nilai_matematika) / len(nilai_matematika)
rata_inggris = sum(nilai_inggris) / len(nilai_inggris)
rata_ipa = sum(nilai_ipa) / len(nilai_ipa)

print(f"Rata-rata nilai Matematika: {rata_matematika:.2f}")
print(f"Rata-rata nilai Bahasa Inggris: {rata_inggris:.2f}")
print(f"Rata-rata nilai IPA: {rata_ipa:.2f}")

print("Function")
# Exercise 1
# The input() function is an example of a:
# a) user-defined function
# b) built-in function
print("Exercise 1:")
print("The input() function is an example of a")
print("b) built-in function")

# Exercise 2
# What happens when you try to invoke a function before you define it?
print("\nExercise 2:")
# hi()  # Uncommenting this line will cause an error due to invoking the function before defining it jadi yang benar itu seperti dibawah

def hi():
    print("hi!")

hi()

# Exercise 3
# What will happen when you run the code below?
print("\nExercise 3:")
def hi():
    print("hi")

# hi(5)  # Uncommenting this akan menimbulkan error sama seperti exercise 2

print("Function Parameter and argument passing")
# Exercise 1
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()
# Output: My name is Bond. James Bond.

# Exercise 2
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")
# Output: My name is Sean Connery. James Bond.

# Exercise 3
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")
# Output: My name is Bond. Susan.

# Exercise 4
# def add_numbers(a, b=2, c):
#     print(a + b + c)
# add_numbers(a=1, c=3)
# kode tersebut akan menyebabkan kesalahan sintaks karena parameter tanpa nilai default (c) diletakkan setelah parameter dengan nilai default (b=2). 
# Dalam Python, parameter tanpa nilai default harus diletakkan terakhir dalam daftar parameter fungsi. 
# Kode tersebut akan menghasilkan kesalahan sintaks dan tidak dapat dijalankan. 

# Jadi solvenya seperti ini
def add_numbers(a, c, b=2):
    print(a + b + c)
add_numbers(a=1, c=3)

print("Retuning Results from Function")
# Exercise 1
def hi():
    return
    print("Hi!")

hi()
# Output: Tidak ada output yang dihasilkan karena pernyataan print() tidak tercapai.

# Exercise 2
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
# Output: True
print(is_int(5.0))
# Output: False
print(is_int("5"))
# Output: None (tidak ada return di kondisi else)

# Exercise 3
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))
# Output: [0, 2, 4, 6, 8, 10]

# Exercise 4
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
# Output: [1, 4, 9, 16, 25]

# Exercise 1
def message():
    alt = 1
    print("Hello, World!")

# The code below will raise a NameError because `alt` is not defined in the global scope.
# print(alt)
# Jadi untuk solvenya ialah menambahkan pernyataan return di dalam fungsi message() dan menampung nilai yang dikembalikan oleh fungsi tersebut ke dalam variabel result, 
# kita bisa dapat mencetak nilai alt yang ada di dalam fungsi message() di luar fungsi tersebut.
# contohnya seperti dibawah

def message():
    alt = 1
    print("Hello, World!")
    return alt

result = message()
print(result)
# Output: 1

# Exercise 2
a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)
# Output: 
# 2
# 1

# Exercise 3
a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)
# Output: 
# 2
# 3

# Exercise 4
a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)
# Output: 
# 2
# 2

print("Creating Simple functions")
# Exercise 1
def factorial(n):
    return n * factorial(n - 1)

# This code will result in a RecursionError. The factorial function doesn't have a base case to stop the recursive calls.
# print(factorial(4))
# jadi untuk solvenya ialah seperti berikut
# perlu menambahkan kondisi dasar atau base case yang akan menghentikan rekursi. 
# Dalam kasus ini, base case adalah saat n sama dengan 0 atau 1, karena nilai faktorial dari 0 atau 1 adalah 1.
# jadi baris codenya seperti dibawah ini

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
# Output: 24
# Dengan menambahkan kondisi dasar if n == 0 or n == 1: return 1, 
# rekursi akan berhenti saat nilai n sama dengan 0 atau 1 
# dan ini akan menghitung faktorial dengan benar untuk nilai n yang valid seperti 4 menjadi 24.

# Exercise 2
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
# Output: 29

print("Tuples and Dictionaries")
# Exercise 1
my_tup = (1, 2, 3)
print(my_tup[2])  # Output: 3

# Exercise 2
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)  # Output: 6

# Exercise 3
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)  # Output: 4

# Exercise 4
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# Exercise 5
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)
print(t)

# Exercise 6
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)

# Exercise 7
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)

# Exercise 8
colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)


try:
    value = int(input("Enter a value: "))
    print(value / value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")  # Menangkap kesalahan umum atau tidak terduga

print("Execption")
try:
    value = int(input("Enter a value: "))
    print(value / value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")  # Menangkap kesalahan umum atau tidak terduga

