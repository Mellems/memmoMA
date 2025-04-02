#matplotlib
import matplotlib.pyplot as plt
# Define data.
xVal = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Make plot graph
plt.scatter(xVal, cubes)

# Set chart title and label axes.
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=18)
plt.ylabel('Cube of Value', fontsize=18)
plt.tick_params(axis="both", labelsize=18)


# Show plot.
plt.show()


#create bigger plot
xVal= list(range(5000))
cubes = [x**3 for x in xVal]


#create plot with parameters
plt.scatter(xVal, cubes, c=cubes, cmap=plt.cm.RdGy, s=20)
#customize plot
plt.title("Cubed", fontsize=24)
plt.xlabel("Values", fontsize=18)
plt.ylabel("Cub of Value", fontsize=18)


#show plot
plt.show()

