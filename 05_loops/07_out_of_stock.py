flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")

print(f"Out side of loop")