import numpy as np
from datetime import datetime

"""
# Leap Year
start_time= datetime.now()
contador=0
for year in range(1000,2000):
  if (year%400==0 or year%4==0 and year%100!=0):
    print(f"{year}")
    contador+=1
print("El total de años bisiestos es:", contador)
end_time= datetime.now()
print("Duration: {}".format(end_time-start_time))
Duration: 0:00:00.002218
"""

#Leap Year Vectorized
start_time= datetime.now()
año= np. arange(start=1000, stop=2000)
print(año[((año%400==0) | (año%4==0) & (año%100!=0))])
end_time= datetime.now()
print("Duration: {}".format(end_time-start_time))
