# Bài 4: Nhập một danh sách các từ cách nhau bởi dấu cách hoặc tab, 
# rồi in ra danh sách và từng phần tử.

ds = input("Danh sách: ").split()

# In cả danh sách vừa nhập
print(ds)

# In từng phần tử trên một dòng
for so in ds:
    print(so)
