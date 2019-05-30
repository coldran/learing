import numpy as np
test = np.array([1, 2, 3, 4, 4, 6, 7, 1, 2, 3, 1])
print(test.shape)
print(np.argmax(np.bincount(test)))

print(np.sort(test))

print(np.linalg.norm(test))

