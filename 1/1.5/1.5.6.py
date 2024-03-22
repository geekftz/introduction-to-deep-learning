import numpy as np

X = np.array([[51, 55], [14, 19], [0, 4]])

for row in X:
    print(row)

X = X.flatten()

print(type(X))
print(X)

print(X[np.array([0, 2, 4])])


print(X > 15)
print(X[X > 15])