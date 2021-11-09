import matplotlib.pyplot as plt
import math

x_cords = []
y_cords = []

for i in range(301):
    value = i/10
    x_cords.append(value)

for j in range(301):
    value = math.sin(x_cords[j])
    y_cords.append(value)

plt.plot(x_cords, y_cords, "b")
plt.show()
