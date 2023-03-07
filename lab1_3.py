name = input("Name:")

lab = input("Lab:")
lab = int(lab)

midterm = input("Midterm:")
midterm = int(midterm)

final = input("Final:")
final = int(final)

lastScore = lab*25/100 + midterm*35/100 + final*40/100

print("*************************")
print("Name:", name)
print("Lab:", lab)
print("Midterm:", midterm)
print("Final:", final)
print("Last Score:", lastScore)