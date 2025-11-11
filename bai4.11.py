# Bước 1: Nhập danh sách các phần tử (chuỗi), cách nhau dấu cách
ds = input("Nhập các phần tử (cách nhau dấu cách): ").split()

# Bước 2: Thêm phần tử 'abc' vào cuối list
ds.append('abc')

# Bước 3: In từng phần tử trong danh sách ra dòng mới
for ch in ds:
    print(ch)
