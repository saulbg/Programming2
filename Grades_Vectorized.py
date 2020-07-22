import numpy as np
from datetime import datetime
"""
# Promedio de calificaciones
start_time=datetime.now()
calif = [10,9,7,8,10,8, 6, 8]
print("Las calificaciones son:", calif)
suma=0
contador=0
promedio=0
for i in calif:
  suma= suma + i
  contador+=1
promedio= suma/contador
print("El promedio es:", promedio)
end_time=datetime.now()
print("Duration: {}".format(end_time-start_time))

Duration: 0:00:00.001388
"""


# Promedio vectorizado
start_time=datetime.now()
calificaciones=np.array([10,9,7,8,10,8,6,8])
print("Las calificaciones son:", calificaciones)
promedio= np.mean(calificaciones)
print("El promedio es:", promedio)
end_time=datetime.now()
print("Duration: {}".format(end_time-start_time))
