# 1. Tách chuỗi thành một list các số nhị phân
binary_numbers = input_str.split(',')

# 2. In ra các giá trị đã được nhập
print("\nCác số nhị phân đã nhập:")
for binary in binary_numbers:
    # Sử dụng .strip() để loại bỏ khoảng trắng thừa nếu có
    print(binary.strip())
