ds = input("Nhập các từ: ").split()

max_len = 0

# Tìm độ dài lớn nhất
for tu in ds:
    if len(tu) > max_len:
        max_len = len(tu)

# In tất cả các từ có độ dài bằng max_len
for tu in ds:
    if len(tu) == max_len:
        print(tu)
