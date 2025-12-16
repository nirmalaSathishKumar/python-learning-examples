age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 or has_license:
    print("You meet one requirement")
else:
    print("You cannot drive")

if not (age < 18):
    print("You are an adult")
