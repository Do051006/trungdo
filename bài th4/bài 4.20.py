# Nhập số n
n = int(input("Nhập số dòng của tam giác Pascal: "))

# Khởi tạo tam giác Pascal
triangle = []

for i in range(n):
    row = [1]  # Mỗi dòng bắt đầu bằng 1
    if i > 0:
        prev_row = triangle[i-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)  # Mỗi dòng kết thúc bằng 1
    triangle.append(row)

# In tam giác Pascal
for row in triangle:
    print(row)
