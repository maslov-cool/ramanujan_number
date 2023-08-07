array = []
# в range пиши вместо 30, то в зависимости от того, сколько тебе нужно чисел Рамануджана
for i in range(1,30):
    for j in range(1,30):
        if i == j:
            continue
        for k in range(1,30):
            if k == i or k == j:
                continue
            for s in range(1,30):
                if s == k or s == i or s == j:
                    continue
                if i ** 3 + j ** 3 == k ** 3 + s ** 3:
                    array.append(i ** 3 + j ** 3)
array = list(set(array))
for g in range(0,len(array)-1):
 min=g
 for t in range(g,len(array)):
        if array[min]>array[t]:
          min=t
 array[g], array[min] = array[min], array[g]
print(array)