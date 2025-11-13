print("\n--- 25. Lọc danh sách theo chỉ mục ---")

# Nhập danh sách từ người dùng
chuoi_danh_sach = input("Nhập các số, cách nhau bằng dấu phẩy: ")
ds = [int(x) for x in chuoi_danh_sach.split(",")]

# Lọc các phần tử ở index 0,2,4,... (tương ứng chỉ số 1,3,5,... nếu bắt đầu từ 1)
ds_loc = ds[0::2]

print("Danh sách sau khi lọc các phần tử theo chỉ mục 1,3,5,... là:")
print(ds_loc)
