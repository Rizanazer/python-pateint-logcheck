a = []
q = []
l = 5
print("enter patient name \n")
for i in range(l):
    name = input("name: ")
    age = input("age: ")

    if name not in a and age not in q:
        a.append(name)
        q.append(age)
    else:
        i = i + 1
        l = l + 1
        print("present")
        print(l)
print(a, q)
