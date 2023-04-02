# x = {"name" : "John", "age" : 36}

# x.get("name")

x = {
    "name": "jina",
    "geniosity": "genius",
    "cake": "chocolate"
}

print()

x["geniosity"]

# print(x.get("cake"))
print(x.items())

print()

for item in x.items():
    print(item)

print("___________________")
print("copy method\n")

y = x.copy()

print(y)

print("___________________")
print("fromkeys method\n")

z = x.fromkeys("name", "nombre")

print(z)
