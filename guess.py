import random
while True:
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        guess_input = input("Tavs minējums: ")
        try:
            guess = int(guess_input)
        except ValueError:
            print("❌ Lūdzu ievadi skaitli!")
            continue
        attempts += 1
        if guess < secret:
            print("Par mazu")
        elif guess > secret:
            print("Par lielu")
        else:
            print(f"🎉 Uzminēji! Skaitlis bija {secret}")
            print(f"Mēģinājumu skaits: {attempts}")
            break
        if attempts >= 10:
            print(f"❌ Mēģinājumi beigušies. Skaitlis bija {secret}")
            break
    again = input("Spēlēt vēlreiz? (j/n): ")
    if again.lower() != "j":
            print("Paldies par spēli!")
            break