# Bước 1: Nhập danh sách các phần tử (chuỗi)
ds = input("Nhập các phần tử (cách nhau dấu cách): ").split()

# Bước 2: Tìm vị trí của phần tử 'abc' nếu có trong list
if 'abc' in ds:
    print("Vị trí của chuỗi 'abc' là", ds.index('abc'))
else:
    print("Không tìm thấy 'abc' trong danh sách"
