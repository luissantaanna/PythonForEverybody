#Calculo de masa corporal

peso = input("Ingrese su peso en kg: ")
p = float(peso)
estatura = input("Ingrese su estatura en metros: ")
est = float(estatura)
masa = p / est**2
imc = float(masa)
print("Su masa corporal es " + str(flaot(imc)))
