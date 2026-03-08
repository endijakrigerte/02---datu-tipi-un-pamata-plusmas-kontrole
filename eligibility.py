age_input = input("Ievadi vecumu: ")

try:
    age = int(age_input)
except ValueError:
    print("❌ Vecumam jābūt skaitlim!")
    exit()

if age < 0:
    print("❌ Vecums nevar būt negatīvs!")
    exit()
license_input = input("Vai ir autovadītāja apliecība? (j/n): ")
student_input = input("Vai ir students? (j/n): ")
veteran_input = input("Vai ir veterāns? (j/n): ")
has_license = license_input.lower() == "j"
is_student = student_input.lower() == "j"
is_veteran = veteran_input.lower() == "j"
can_vote = age >= 18
can_rent_car = age >= 21 and has_license
senior_discount = age >= 65 or is_veteran
student_discount = 16 <= age <= 26 and is_student
vote_text = "Jā ✓" if can_vote else "Nē ✗"
rent_text = "Jā ✓" if can_rent_car else "Nē ✗"
if not has_license and age >= 21:
    rent_text = "Nē ✗ (nav apliecības)"
senior_text = "Jā ✓" if senior_discount else "Nē ✗"
student_text = "Jā ✓" if student_discount else "Nē ✗"
print("---")
print(f"Balsošana:        {vote_text}")
print(f"Auto īre:         {rent_text}")
print(f"Senioru atlaide:  {senior_text}")
print(f"Studentu atlaide: {student_text}")