nota = float(input("Ingrese su nota: "))
if nota >60:
    print ("!Felicidades aprobaste¡")
else:
    print("Perdiste papu") 

def Notas():
    lista =[]
    try:
        nota =  (input("Ingrese sus nota crack ")).split(",")
        """print(f"nota= {nota}, type {type(nota)} variable dentro de la lista {type(nota[0])}")"""
        #nota = float(nota)
        lista =[float(x)for x in nota]
        numero_mas_grande = max(nota)
        print(f"esta es su mayor nota: {numero_mas_grande}")

    except ValueError:
        print("error69")
    return lista



lista = Notas()
print(lista)


def promedios (lista_p):
    promedio = round (sum(lista_p)/len(lista_p),2)
    print(f"su promedio: {promedio}")
    
    return promedio


perrito = promedios(lista)

















    
    


