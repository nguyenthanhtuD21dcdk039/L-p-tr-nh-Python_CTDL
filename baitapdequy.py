def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n - 1)


a = int(input("Nhập vào 1 số tự nhiên: "))
ket_qua = giai_thua(a)
print(f"Kết quả tính được là: {a}! = {ket_qua}")
