ds = input("Nhập các số: ").split()

# Chuyển các phần tử từ chuỗi sang số nguyên
ds = [int(x) for x in ds]

tong_chan = 0

for so in ds:
    if so % 2 == 0:
        tong_chan += so

print("Tổng các số chẵn:", tong_chan)
