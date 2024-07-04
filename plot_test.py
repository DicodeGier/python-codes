import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure()
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Save the plot to a file
plt.savefig("CAE/sine_wave.png")

# Close the plot to free up memory
plt.close()

# Rest of your code
print("Plot saved and code continues to run.")