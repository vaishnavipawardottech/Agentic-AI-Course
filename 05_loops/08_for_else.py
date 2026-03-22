staff = [("Vaishnavi", 22), ("dattatray", 47), ("shubhangi", 43)]

for name, age in staff:
    if age > 50:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")