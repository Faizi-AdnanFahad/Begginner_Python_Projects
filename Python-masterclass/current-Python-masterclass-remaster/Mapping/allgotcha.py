entries = []

print(f"all: {all(entries)}")  # True
print(f"any: {any(entries)}")  # False

if entries:
    print("hi")

result = entries and all(entries)
print(result)  # []

result = bool(entries) and all(entries)
print(result)  # False