import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))

# Use of for loop in list declaration
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()

# Defining values for scatter, also defining line thickness, color gradient, etc)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title ane label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Customize the range of the axes
ax.axis([0, 1000, 0, 1100000])

plt.show()

# Ability to save plot to a png file
# plt.savefig('squares_plot.png', bbox_inches='tight')
