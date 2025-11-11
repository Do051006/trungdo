Return Sum_of_divisors > num

try:
    n = int(input("Nhập số nguyên dương n: "))
    
    print(f"\nCác số nguyên dương nhỏ hơn {n} có tổng các ước lớn hơn chính nó là:")
    
    # Số hoàn thiện thừa nhỏ nhất là 12, nên bắt đầu từ 12
    for i in range(1, n):
        if kiem_tra_so_hoan_thien_thua(i):
            print(i)

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
