clientes1= list(("Alemania","Reino Unido","Portugal","Afganistan"))



print(type(clientes1))
print(list)
print(clientes1)

clientes2=["paco","fernando","jose","roberto",]
print(type(clientes2))
print(clientes2)
clientes2[1]="paco chocolatero"
print(clientes2)
lista3= clientes1 + clientes2
print(lista3)
print(clientes1[0])
print(clientes1[-1])
print(clientes1[1:4])
print(clientes1[:3])
print("____________o______________")
lista3.extend(clientes1)
print(lista3)
clientes4=["huevos","salchicha","pavo"]
print("____________%%%%___________")
print(clientes4)
print(type(clientes4))
print("_________o_________________")
print(clientes1)
####.pop() borra el ultimo objeto de la lista###
clientes1.pop()
print(clientes1)
print("___________&___________")

clientes1.pop()
print(clientes1)
