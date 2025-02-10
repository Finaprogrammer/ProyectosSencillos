#concatenar cadenas de caracteres
#supongamos que queremos crear una cadena que diga:
#aprende a progreamar con _____.

organizacion = "finaprosa"

#print("aprende a programar con " + organizacion)
#print(f"aprende a programar con {organizacion}") #f-string

adj=input("ingresa un adjetivo: ")
verbo1=input("ingresa un verbo: ")
sustantivo=input("ingresa un sustantivo en plural: ")


madlib = f"programar es tan {adj}! siempre me emociona por que me encanta {verbo1}¡aprende para alcanzar tus {sustantivo}"

print(madlib)


