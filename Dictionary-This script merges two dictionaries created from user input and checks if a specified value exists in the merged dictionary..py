def create(u):
    a = u.split(',')
    d = {}
    for i in a:
        key, value = i.split(':')
        d[key.strip()] = value.strip()
    return d
p = input("Enter elements for 1st dictionary ")
d1 = create(p)
q = input("Enter elements for 2nd dictionary ")
d2 = create(q)
d1.update(d2)
d3 = d1
print("Merged dictionary:", d3)
def check(value):
    if value in d3.values():
        print("Value already exists")
    else:
        print("Value doesn't exist")

x = input("Enter a value to check: ")
check(x)
