#ejercicio 5 #########################
milista=["s","m", "i","l","e"]
#convertir a string con separacion - y sin corchetesº
resultado="-".join(milista)
print(resultado)

#5 
PT="smile"
#convertir a lista
lista=[]
for letra in PT:
    lista.append(letra)
print(lista)    

#opcion2

lista2=[letra for letra in PT]
print(lista2)

#opcion3
lista3=PT.split()
print(lista3)

#opcion4
i=0
lista_while=[]
while i < len(PT):
    lista_while+=PT[i]
    i+=1
print(lista_while)

#opcion5 com map
lista_map=list(map(lambda i:i, PT))
    
def f(x):
    if x == 0:
        return 0
    return x + f(x-1)#esto se opera dentro del parentesis y se llama a si misma
"""es recursiva se llama a si misma
primera vuelta 3 +(2)
segunda vuelta 2 +(1)
tercera        1+(0) resultado=6"""
print(f(3))
print("==============================================================================================================================================================================")
print("\n")

listado=[(1,"manzana"),(2,"pera"),(3,"uva"),(4,"sandia"),(5,"melon"),
(6,"cereza"),(7,"platano"),(8,"kiwi"),(9,"fresa"),(10,"naranja"),
(11,"mandarina"),(12,"pomelo"),(13,"limon"),(14,"mango"),(15,"coco"),
(16,"piña"),(17,"frambuesa"),(18,"arandano"),(19,"moras"),(20,"frutilla"),
(21,"papaya"),(22,"granada"),(23,"higo"),(24,"ciruela"),(25,"albaricoque"),
(26,"cereza"),(27,"platano"),(28,"kiwi"),(29,"fresa"),(30,"naranja"),
(31,"mandarina"),(32,"pomelo"),(33,"limon"),(34,"mango"),(35,"coco"),
(36,"piña"),(37,"frambuesa"),(38,"arandano"),(39,"moras"),(40,"frutilla"),
(41,"papaya"),(42,"granada"),(43,"higo"),(44,"ciruela"),(45,"albaricoque"),
(46,"cereza"),(47,"platano"),(48,"kiwi"),(49,"fresa"),(50,"naranja"),
(51,"mandarina"),(52,"pomelo"),(53,"limon"),(54,"mango"),(55,"coco"),
(56,"piña"),(57,"frambuesa"),(58,"arandano"),(59,"moras"),(60,"frutilla"),
(61,"papaya"),(62,"granada"),(63,"higo"),(64,"ciruela"),(65,"albaricoque"),
(66,"cereza"),(67,"platano"),(68,"kiwi"),(69,"fresa"),(70,"naranja"),
(71,"mandarina"),(72,"pomelo"),(73,"limon"),(74,"mango"),(75,"coco"),
(76,"piña"),(77,"frambuesa"),(78,"arandano"),(79,"moras"),(80,"frutilla"),
(81,"papaya"),(82,"granada"),(83,"higo"),(84,"ciruela"),(85,"albaricoque"),
(86,"cereza"),(87,"platano"),(88,"kiwi"),(89,"fresa"),(90,"naranja"),
(91,"mandarina"),(92,"pomelo"),(93,"limon"),(94,"mango"),(95,"coco"),
(96,"piña"),(97,"frambuesa"),(98,"arandano"),(99,"moras"),(100,"frutilla")
 ]
#ordenar por nombre de fruta resultado en orden alfabetico[(25, 'albaricoque'), (45, 'albaricoque'), (65, 'albaricoque'),
# (85, 'albaricoque'), (18, 'arandano'), (38, 'arandano'), (58, 'arandano'), (78, 'arandano'), (98, 'arandano'), (6, 'cereza'),
# (26, 'cereza'), (46, 'cereza'), (66, 'cereza'), (86, 'cereza'), (24, 'ciruela'), (44, 'ciruela'), (64, 'ciruela'), (84, 'ciruela'),
# (15, 'coco'), (35, 'coco'), (55, 'coco'), (75, 'coco'), (95, 'coco'), (17, 'frambuesa'), (37, 'frambuesa'), (57, 'frambuesa'),
# (77, 'frambuesa'), (97, 'frambuesa'), (9, 'fresa'), (29, 'fresa'), (49, 'fresa'), (69, 'fresa'), (89, 'fresa'), (20, 'frutilla'),
# (40, 'frutilla'), (60, 'frutilla'), (80, 'frutilla'), (100, 'frutilla'), (22, 'granada'), (42, 'granada'), (62, 'granada'),
# (82, 'granada'), (23, 'higo'), (43, 'higo'), (63, 'higo'), (83, 'higo'), (8, 'kiwi'), (28, 'kiwi'), (48, 'kiwi'), (68, 'kiwi'),
# (88, 'kiwi'), (13, 'limon'), (33, 'limon'), (53, 'limon'), (73, 'limon'), (93, 'limon'), (11, 'mandarina'), (31, 'mandarina'),
# (51, 'mandarina'), (71, 'mandarina'), (91, 'mandarina'), (14, 'mango'), (34, 'mango'), (54, 'mango'), (74, 'mango'), (94, 'mango'),
# (1, 'manzana'), (5, 'melon'), (19, 'moras'), (39, 'moras'), (59, 'moras'), (79, 'moras'), (99, 'moras'), (10, 'naranja'), 
# (30, 'naranja'), (50, 'naranja'), (70, 'naranja'), (90, 'naranja'), (21, 'papaya'), (41, 'papaya'), (61, 'papaya'), (81, 'papaya'),
# (2, 'pera'), (16, 'piña'), (36, 'piña'), (56, 'piña'), (76, 'piña'), (96, 'piña'), (7, 'platano'), (27, 'platano'), (47, 'platano'), 
# (67, 'platano'), (87, 'platano'), (12, 'pomelo'), (32, 'pomelo'), (52, 'pomelo'), (72, 'pomelo'), (92, 'pomelo'), (4, 'sandia'), (3, 'uva')]
listado.sort(key=lambda i:i[1])

print(listado)

for elemento in listado:
    print(elemento[0], '\n', elemento[1])
print("fin de la lista")

class Yo():
    pass
if __name__=="__main__":
    print("Soy el modulo examen me imprimo solo si me ejecuto como principal")
     
    print(Yo.__name__)
else:
    print("Soy el modulo examen me imprimo solo si me ejecuto como modulo exportado")
    
# print(dir(Yo))
# help(Yo)
print(Yo.__dict__)

print(f"lista_map: {lista_map}")