ds = ["123", "456", "789", "123"]
print("List gốc:", ds)

# Sử dụng phương thức .remove() để xóa phần tử đầu tiên có giá trị là '123'
ds.remove('123')

print("List sau khi xóa:")
for ch in ds:
    print(ch)
