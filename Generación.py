year=eval(input("¿En qué año naciste?: "))
if year<1930:
    print("Favor de introducir un año válido")
elif year<=1948:
    print("Eres parte de la generación silenciosa")
elif year<=1968:
    print("Eres parte de la generación Baby Boom")
elif year<=1980:
    print("Eres parte de la generación X")
elif year<=1995:
    print("Eres parte de la generación Millenial")
elif year<2021:
    print("Eres parte de la generación Z")
else:
    print("Ese año todavía no ha pasado, no seas pentiroso")