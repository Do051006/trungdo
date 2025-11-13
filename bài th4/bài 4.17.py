def sum_of_proper_divisors(x):
    """Trả về tổng các ước riêng (không bao gồm x) của x."""
    if x <= 1:
        return 0
    s = 1  # 1 luôn là ước riêng của mọi x > 1
    # ta có thể lặp từ 2 tới sqrt(x) để tìm cặp ước
    import math
    r = int(math.sqrt(x))
    for d in range(2, r+1):
        if x % d == 0:
            s += d
            other = x // d
            if other != d:
                s += other
    return s

def is_abundant(x):
    """Kiểm tra xem x có phải là số abundant không."""
    return sum_of_proper_divisors(x) > x

def main():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.")
            return

        print(f"\nCác số nguyên dương nhỏ hơn {n} có tổng các ước riêng lớn hơn chính nó là:")
        for i in range(1, n):
            if is_abundant(i):
                print(i)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()
