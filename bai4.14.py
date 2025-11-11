# Bước 1: Nhập danh sách các phần tử (chuỗi)
ds = input("Nhập các phần tử (cách nhau dấu cách): ").split()

# Bước 2: Sắp xếp danh sách theo thứ tự tăng dần (theo bảng chữ cái)
ds.sort()

# Bước 3: In từng phần tử trong danh sách ra dòng mới
for ch in ds:
    print(ch)
