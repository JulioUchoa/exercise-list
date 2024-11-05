lt = []
tl = []
for i in range(10):
    lt.append(i)
    if i < 5:
        tl.append(i)
print(tl)
print(lt)
print(lt[0:5])
if lt[0:5] == tl:
    print('ok')

