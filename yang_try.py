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

