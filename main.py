from calculadora_DNI import calculadora_dni
numero_dni = "12345678"
letra_dni = calculadora_dni(numero_dni)
print(f"dni calculado: {numero_dni}-{letra_dni}") 

n = int(input ("introduzca el numero del DNI:"))
letra = "T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"
print("la letra del DNI es:", letra[n%23])

#from calculadora_DNI import calculadora_dni
#def pide_un_numero():
#   msg = "Dame un num: "
#   entrada = ''
#   invalido = False
#   numero = -1
#   while not entrada.isnumeric():
#       if invalido:
#           print("Obligatoriamente debe ser un número")
#       invalido = True
#       entrada = input(msg)
#   return int(entrada)
#numero_DNI = pide_un_numero Max8Digitos
#letra_dni = calculadora_DNI(numero_dni)
#print(f"DNI calculado: {numero_DNI}-{letra_dni}")
