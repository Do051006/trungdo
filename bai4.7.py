S = input("Nhập chuỗi: ")

kq = ""  # Chuỗi kết quả

# Duyệt qua từng ký tự
for ch in S:
    if not ch.isdigit():  # isdigit() trả về True nếu ký tự là số
        kq += ch

print("Chuỗi sau khi loại bỏ chữ số:", kq)
