#Program To Find Common Elements In Two Lists Irrespective Of Their List Size

a = [2,5,6,2,8,9,23,45]
b = [6,8,9,43,67,87]
c=[]


for i in a[::]:
    for j in b[::]:
        if i == j and i not in c:
            c.append(i)

print(c)
