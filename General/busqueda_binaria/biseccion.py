import bisect as bs

lista = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]

print(bs.bisect_left(lista, 5)) # 2
print(bs.bisect_right(lista, 5)) # 3
