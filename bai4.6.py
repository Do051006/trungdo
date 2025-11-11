hoten = input("Nhập họ và tên: ")

# Tách chuỗi họ tên thành các phần tử (các từ)
ds = hoten.split()

# Giả thiết họ và tên riêng chỉ gồm một từ
ho = ds[0]
ten = ds[1]

# In kết quả
print("Họ:", ho)
print("Tên:", ten)
