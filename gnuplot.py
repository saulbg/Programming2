import matplotlib.pyplot as plt
import pandas as pd

# Opening the files and reading them as a data frame
eje_x = pd.read_csv('wktime.T001.his', delimiter=' ', header = None)
eje_y = pd.read_csv('wktime.T004.his',delimiter=' ',header= None)

# Defining the plots with different colors and labels.
plt.plot(eje_x[0], eje_x[1], color = 'r', label = 'Time 1') 
plt.plot(eje_y[0], eje_y[1], color = 'b', label = 'Time 4') 

# Putting the name on the graph to the axis x and axis y
plt.xlabel('Wealth')
plt.ylabel('Probability')

# Setting an scale to logarithmic
plt.xscale("log"), plt.yscale("log")

#Setting the limits to be shown of the axis
plt.xlim((0.000001, 100.0)) 
plt.ylim((0.000001, 100000.0))

# Plotting legend
plt.legend()
# Display plot 
plt.show() 
