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
lista3.extend(clientes2)
print(lista3)
variable1 = lista3
variable2 = lista3.copy()
print(id(lista3))
print(id(variable1))
print(id(variable2))
