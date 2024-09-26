def create_list_inversa(n):
    strange_list = []
    for i in range(0, n):            #range(0,n) equivale [0, 1, 2, ..., n-1]
        strange_list.insert(0, i)    #append inverso  1º vuelta [0] 2º vuelta [1,0] 
    return strange_list
    
def create_list(n):
    strange_list = []
    for i in range(0, n):            #range(0,n) equivale [0, 1, 2, ..., n-1]
        strange_list.append(i)    #append inverso  1º vuelta [0] 2º vuelta [1,0] 
    return strange_list

def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

if __name__ == "__main__":
    
  resultado = 0
  listaresultante = create_list_inversa(20)
  print(listaresultante)
  resultado= list_sum(listaresultante)
  print(resultado)
  
  print(list_sum(create_list_inversa(20)))
  

  
   
