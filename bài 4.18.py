# Nhập số n
n = int(input("Nhập số lượng phần tử Fibonacci: "))

# Khởi tạo danh sách Fibonacci
fibo = []

# Tạo dãy Fibonacci
a, b = 0, 1
for i in range(n):
    fibo.append(a)
    a, b = b, a + b

# In kết quả
print("Danh sách", n, "số Fibonacci đầu tiên là:")
for num in fibo:
    print(num)
