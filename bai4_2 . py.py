

# Bài 2: In ra từng ký tự nhưng bỏ qua ký tự không nhìn thấy

S = input("Nhập chuỗi S: ")

for ch in S:
    if ch not in [' ', '\t']:
        print(ch)
