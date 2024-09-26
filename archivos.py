try:

    with open("archivo.txt", "a", encoding="utf-8") as archivo:
    
        archivo.write("Hola mundo")
        archivo.write("\n")
        archivo.write("Hola mundofocugeWIHGIHBVIRFOjbo jgtòeqajhtpknp+akjt0qa'khtn`pkq'ih'5¡6iq'¡htbàpkpknpkqa'rfàh+`thk0wi45'i'ui'iy'¡3i44'i'2iyIGR'AKPKBÑNEKAKKPAKH`PFKHPÀKTEPKHP")
       
except FileNotFoundError as e:
    print("ocurrio un error al abrir el archivo", e, type(e))
    
    
try:
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        contenido=archivo.read()
        print(contenido)
except FileNotFoundError as e:
    print("ocurrio un error al abrir el archivo", e, type(e))
    