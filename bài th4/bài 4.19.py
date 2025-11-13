# Nhập n
n = int(input("Nhập số n: "))

# Hàm tính tổng các ước số thực sự của x
def sum_of_divisors(x):
    total = 0
    for i in range(1, x):
        if x % i == 0:
            total += i
    return total

# Tạo list các số vượt
abundant_numbers = []
for num in range(1, n):
    if sum_of_divisors(num) > num:
        abundant_numbers.append(num)

# Chuyển list sang tuple
p = tuple(abundant_numbers)

# In kết quả
print("Tuple p gồm các số vượt nhỏ hơn", n, "là:")
print(p)
