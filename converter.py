# Konstantes
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020
print("Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) USD <-> EUR")

choice = input("> ")
print("Virziens:")
print("1) uz priekšu")
print("2) atpakaļ")

direction = input("> ")
value_input = input("Ievadi vērtību: ")

try:
    value = float(value_input)
except ValueError:
    print("❌ Lūdzu ievadi skaitli!")
    exit()
if choice == "1":  # km ↔ mi
    if direction == "1":
        result = value * KM_TO_MI
        print(f"{value:.2f} km = {result:.2f} mi")
    elif direction == "2":
        result = value / KM_TO_MI
        print(f"{value:.2f} mi = {result:.2f} km")
    else:
        print("❌ Nepareizs virziens")

elif choice == "2":  # kg ↔ lb
    if direction == "1":
        result = value * KG_TO_LB
        print(f"{value:.2f} kg = {result:.2f} lb")
    elif direction == "2":
        result = value / KG_TO_LB
        print(f"{value:.2f} lb = {result:.2f} kg")
    else:
        print("❌ Nepareizs virziens")

elif choice == "3":  # L ↔ gal
    if direction == "1":
        result = value * L_TO_GAL
        print(f"{value:.2f} L = {result:.2f} gal")
    elif direction == "2":
        result = value / L_TO_GAL
        print(f"{value:.2f} gal = {result:.2f} L")
    else:
        print("❌ Nepareizs virziens")

elif choice == "4":  # USD ↔ EUR
    if direction == "1":
        result = value * USD_TO_EUR
        print(f"{value:.2f} USD = {result:.2f} EUR")
    elif direction == "2":
        result = value / USD_TO_EUR
        print(f"{value:.2f} EUR = {result:.2f} USD")
    else:
        print("❌ Nepareizs virziens")
else:
    print("❌ Nepareiza izvēle")