print("\n--- 23. Đếm chữ cái và chữ số trong câu ---")

# Nhập câu từ người dùng
cau = input("Nhập một câu: ")

so_chu_cai = 0
so_chu_so = 0

for ky_tu in cau:
    if ky_tu.isalpha():
        so_chu_cai += 1
    elif ky_tu.isdigit():
        so_chu_so += 1

print(f"Chữ cái: {so_chu_cai}, Chữ số: {so_chu_so}")
