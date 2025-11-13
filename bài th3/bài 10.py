import math

def Tinh(R):
    """
    Hàm này kiểm tra tính hợp lệ của bán kính R,
    sau đó tính và in ra chu vi và diện tích của hình tròn.
    """
    if R <= 0:
        print("Lỗi: Bán kính phải là một số dương. Vui lòng nhập lại.")
        return

    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    print("--- KẾT QUẢ ---")
    print(f"Với bán kính R = {R}:")
    print(f"-> Chu vi hình tròn là: {chu_vi:.2f}")
    print(f"-> Diện tích hình tròn là: {dien_tich:.2f}")

try:
    R_nhap_vao = float(input("Vui lòng nhập vào bán kính R của hình tròn: "))
    
    Tinh(R_nhap_vao)
    
except ValueError:
    print("Lỗi: Đầu vào không phải là một số. Vui lòng chạy lại chương trình.")
