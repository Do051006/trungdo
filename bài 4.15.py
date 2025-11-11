# Yêu cầu người dùng nhập chuỗi
input_str = input("Nhập liên tiếp các từ tiếng Anh (cách nhau bởi dấu cách): ")

# 1. Tách chuỗi thành một list các từ
list_of_words = input_str.split()

# 2. Sắp xếp list các từ theo thứ tự từ điển (alphabetical order)
list_of_words.sort()

# 3. In ra các từ đã được sắp xếp
print("\nCác từ sau khi sắp xếp theo thứ tự từ điển:")
for word in list_of_words:
    print(word)
