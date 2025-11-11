print("\n--- 26. Tính số dư tài khoản ngân hàng ---")

so_du = 0

print("Nhập nhật ký giao dịch (mỗi giao dịch một dòng, 'D <số>' hoặc 'W <số>').")
print("Nhập dòng trống để kết thúc.")

while True:
    giao_dich = input()
    if giao_dich == "":  # Dòng trống để kết thúc nhập
        break
    try:
        loai, so_tien = giao_dich.split()
        so_tien = int(so_tien)
        if loai.upper() == "D":
            so_du += so_tien
        elif loai.upper() == "W":
            so_du -= so_tien
        else:
            print(f"Bỏ qua giao dịch không hợp lệ: {giao_dich}")
    except ValueError:
        print(f"Bỏ qua giao dịch không hợp lệ: {giao_dich}")

print(f"Số dư cuối cùng của tài khoản là: {so_du}")
