def dao_nguoc(chuoi):
    return chuoi[::-1]
input_string = input("Nhập chuỗi bạn muốn đảo ngược đi: ")
print("Chuỗi đảo ngược là: ", dao_nguoc(input_string))