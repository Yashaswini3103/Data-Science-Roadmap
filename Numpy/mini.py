import numpy as np

marks = np.array([85,90,78,92,60,88,95])
print("data type:", marks.dtype)
print("shape:", marks.shape)

new_marks=marks.reshape(7,1)
print(new_marks)

print("sorted marks:", np.sort(marks))
print("top 5 marks:",np.sort(marks)[-5:][::-1])

print(marks[marks>80])

for rows in marks:
    print(rows)