import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]

y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y, c ="blue")

x1 = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20]

y1 = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10]

x2 = [26, 29, 48, 64, 6, 5, 36, 66, 72, 40]

y2 = [26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

plt.scatter(x1, y1, c ="pink", linewidths = 2, marker ="s", edgecolor ="green", s = 50)

plt.scatter(x2,  y2, c ="pink", linewidths = 2, marker ="^", edgecolor ="red", s = 200)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()