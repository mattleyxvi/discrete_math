#el primo       на выводе построенные дороги
pts = input().split(" ")#названия точек
roads = input().split(" ")#дороги из названий дорог типа ab
lngth = input().split(" ")#длина соответсвующих дорог
chroads = []
snlngth = []
asc = True
class1 = -1
class2 = -1
for i in lngth:#отсортированный по длине массив
    snlngth.append(int(i))
snlngth.sort()
eq = [[roads[lngth.index(str(snlngth[0]))][0],roads[lngth.index(str(snlngth[0]))][1]]] #
chroads.append(roads[lngth.index(str(snlngth[0]))])
for i in snlngth:
    b = roads[lngth.index(str(i))]
    for ind in range(0,len(eq)):#определяем классы начала и конца дороги
        if b[0] in eq[ind]:
            class1 = ind
        if b[1] in eq[ind]:
            class2 = ind
    print(class1,class2)
    if class1==class2 and class1==-1:#если оба ни в одном из классов
        eq.append([b[0],b[1]])
    elif class1!=class2 and (class1==-1 or class2==-1):#если только один без класса
        if class1==-1:
            eq[class2].append(b[0])
        elif class2==-1:
            eq[class1].append(b[1])
    elif class1!=class2 and class1!=-1 and class2!=-1:#если оба в разных классах
        for obj in eq[max(class1,class2)]:
            eq[min(class1,class2)].append(obj)
        eq[max(class1,class2)]=[]
    if class1==class2 and class1!=-1:#если в одинаковом то не подходит
        class1 = -1
        class2 = -1
        lngth[lngth.index(str(i))]='0'
        continue
    chroads.append(b)
    lngth[lngth.index(str(i))]='0'#зануляем чтобы если есть одинаковые длины не выдавали одну дорогу
    class1 = -1
    class2 = -1
print(chroads)
print(eq)            
