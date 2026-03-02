# Pamatdatu tipi
text1 = "Sveiki"
text2 = "Python"

number1 = 5
number2 = 10

decimal1 = 3.14
decimal2 = 2.5

flag1 = True
flag2 = False

empty_value = None

# Tipu pārbaude
print(type(text1))
print(type(number1))
print(type(decimal1))
print(type(flag1))
print(type(empty_value))

# Truthy / Falsy piemēri
print(bool(""))       # False
print(bool(" "))      # True
print(bool("0"))      # True
print(bool(0))        # False
print(bool([]))       # False
print(bool(None))     # False

# Virkņu savienošana
print("5" + "3")
# print("5" + 3)  # TypeError
print(int("5") + 3)

# Robežgadījumi
# print(int("abc"))  # ValueError
print(float("3.14"))

# Jauktā aritmētika
print(True + True)
print(True * 10)
print(False + 5)
print(10 / True)

# Skaitļu pārveidošana
print(int(3.86))
# print(int("3.14"))  # ValueError
print(int(float("3.14")))
print(float("1e3"))

# Interesanti gadījumi
print(0.1 + 0.2 == 0.3)
print(round(2.5))
print(round(3.5))