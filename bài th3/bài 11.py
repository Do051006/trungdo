def benefit(n, k, rate):
    total = n * (1 + rate/100) ** k
    return total

n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))
rate = float(input("Nhập lãi suất (%/tháng): "))

money = benefit(n, k, rate)
print("Số tiền nhận được sau", k, "tháng là:", round(money, 2))
