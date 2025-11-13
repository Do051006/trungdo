"""Program make a simple calculator that can add, subtract, multiply and 
divide using functions"""
# This function adds two numbers
# Hàm này cộng hai số
def ham_cong(x, y):
    return x + y 
# This function subtracts two numbers  
def ham_tru(x, y):
    return x - y 
# This function multiplies two numbers 
def ham_nhan(x, y):
    return x * y 
# This function divides two numbers 
def ham_chia(x, y):
    return x / y 
print("lựa chọn cách sau.") 
print("1.Add") 
print("2.ham_tru") 
print("3.ham_nhan") 
print("4.ham_chia") 
# Take input from the user  
choice = input("Enter choice(1/2/3/4):") 
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
if choice == '1':
    print(num1,"+",num2,"=", ham_cong(num1,num2)) 
elif choice == '2':
    print(num1,"-",num2,"=", ham_tru(num1,num2)) 
elif choice == '3':
    print(num1,"*",num2,"=", ham_nhan(num1,num2)) 
elif choice == '4':
    print(num1,"/",num2,"=", ham_chia(num1,num2)) 
else:
    print("Invalid input")
