ds = input("Danh sách: ").split()

# In danh sách gốc
print("Danh sách ban đầu:", ds)

# Đảo ngược thứ tự
ds.reverse()

# In danh sách đã đảo ngược
print("Danh sách sau khi đảo:", ds)

# In từng phần tử trên một dòng
for so in ds:
    print(so)
