# Bước 1: Nhập danh sách các phần tử (chuỗi)
ds = input("Nhập các phần tử (cách nhau dấu cách): ").split()

# Bước 2: Kiểm tra nếu phần tử '123' có trong danh sách thì xóa nó
if '123' in ds:
    ds.remove('123')

# Bước 3: In từng phần tử trong danh sách ra dòng mới
for ch in ds:
    print(ch)
