import pandas as pd

print("Estas son las calificaciones del maestro de programación \n")
califA = pd.Series([8, 8, 9, 7, 5, 10, 10, 9, 8, 9, 9, 7])
califB = pd.Series([6, 5, 9, 8, 5, 8, 10, 9, 8, 6])

califA.name= 'Calificaciones A'
califB.name= 'Calificaciones B'

print(califA)
print(califB)
print("")

calif2 = pd.DataFrame({'A': califA, 'B': califB})
print(calif2.head())
print("")

meanA=calif2['A'].mean()
print("El promedio del grupo A es:",meanA)
print("")

meanB=calif2['B'].mean()
print("El promedio del grupo B es:", meanB)
print("")

repA=califA.value_counts()
print("En el grupo A las calificaciones se repiten:\n", repA)
print("")

repB=califB.value_counts()
print("En el grupo B las calificaciones se repiten:\n", repB)
