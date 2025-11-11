print("\n--- 22. Tìm các số có tất cả chữ số chẵn trong khoảng 1000-3000 ---")

# Danh sách lưu các số thỏa mãn
ds_chan = []

for so in range(1000, 3001):
    chuoi = str(so)
    # Kiểm tra tất cả chữ số đều chẵn
    if all(int(ch) % 2 == 0 for ch in chuoi):
        ds_chan.append(so)

# In kết quả
print("Các số có tất cả chữ số chẵn từ 1000 đến 3000 là:")
print(ds_chan)
