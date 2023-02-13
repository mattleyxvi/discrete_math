#el primo       на выводе построенные дороги
pts = input().split(" ")#названия точек
roads = input().split(" ")#дороги из названий дорог типа ab
lngth = input().split(" ")#длина соответсвующих дорог
usdpts = [pts[0]]
chroads = []
snlngth = []
snindex = []
while(len(usdpts)!=len(pts)):
    for i in roads:
        for j in usdpts:
            b = i
            if j in i and not b.replace(j,'') in usdpts:
                snindex.append(roads.index(i))
                snlngth.append(int(lngth[roads.index(i)]))
    a = snindex[snlngth.index(min(snlngth))]
    chroads.append(roads[a])
    for q in roads[a]:
        if not q in usdpts:
            usdpts.append(q)
    snindex.clear()
    snlngth.clear()
print(chroads)
            
