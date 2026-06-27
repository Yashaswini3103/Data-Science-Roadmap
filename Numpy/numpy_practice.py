import numpy as np

marks = np.array([
    [85, 90],
    [78, 92],
    [60,88],
    [95,98]
])

print("maths marks:", marks[:,0])
print("science marks:", marks[:,1])
print("maths average:", np.mean(marks[:,0]))
print("science average:", np.mean(marks[:,1]))
print("maths>80:",marks[marks[:,0]>80])
print("science>90:",marks[marks[:,1]>90])