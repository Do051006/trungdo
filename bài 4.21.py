print("\n--- 21. Kiểm tra số nhị phân 4 chữ số chia hết cho 5 ---")

# Nhập chuỗi nhị phân
chuoi_nhi_phan = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")

# Tách thành danh sách
ds_nhi_phan = chuoi_nhi_phan.split(",")

# Danh sách lưu các số chia hết cho 5
ds_chia_het_5 = []

for so in ds_nhi_phan:
    try:
        if len(so) == 4:  # chỉ xét số nhị phân 4 chữ số
            thap_phan = int(so, 2)  # chuyển sang thập phân
            if thap_phan % 5 == 0:
                ds_chia_het_5.append(so)
        else:
            print(f"Bỏ qua {so}: không phải 4 chữ số")
    except ValueError:
        print(f"Bỏ qua {so}: không phải số nhị phân hợp lệ")

# In kết quả
print("Các số nhị phân chia hết cho 5 là:")
print(",".join(ds_chia_het_5))
