"""
x = input("Nhập vào giá trị của x = ")
x = int(x)

if x > 0:
    print(x, "là số dương")
if x % 2 == 0:
    print(x, "cũng là số chẵn")
else:
    print(x, "cũng là số lẽ")
print("Kết thúc chương trình")

x = input("Nhập điểm tổng kết: ")
x = float(x)
if x >= 8.0:
    print(x, "Đủ điều kiện học sinh giỏi")
elif x >= 6.5:
    print(x, "Đủ điều kiện học sinh Khá")
elif x >= 5.0:
    print(x, "Đủ điều kiện học sinh Trung Bình")
else:
    print(x, "Đạt danh hiệu học sinh Kém")
print("Kết thúc chương trình")
"""
import math

Toan = float(input("Nhập vào điểm trung bình cuối kỳ của môn Toán = "))
Ly = float(input("Nhập vào điểm trung bình cuối kỳ của môn Lý = "))
Hoa = float(input("Nhập vào điểm trung bình cuối kỳ của môn Hóa = "))
Ngu_Van = float(input("Nhập vào điểm trung bình cuối kỳ của môn Ngữ Văn = "))
Tieng_Anh = float(input("Nhập vào điểm trung bình cuối kỳ của môn Tiếng Anh = "))
Su = float(input("Nhập vào điểm trung bình cuối kỳ của môn Lịch Sử = "))
Dia = float(input("Nhập vào điểm trung bình cuối kỳ của môn Địa Lý = "))
Sinh_Hoc = float(input("Nhập vào điểm trung bình cuối kỳ của môn Sinh Học = "))
GDCD = float(input("Nhập vào điểm trung bình cuối kỳ của môn Giáo Dục Công Dân = "))
GDQPAN = float(
    input("Nhập vào điểm trung bình cuối kỳ của môn Giáo Dục Quốc Phòng An Ninh = ")
)
GDTC = float(input("Nhập vào điểm trung bình cuối kỳ của môn Giáo Dục Thể Chất = "))
Tin_Hoc = float(input("Nhập vào điểm trung bình cuối kỳ của môn Tin Học = "))

if ((Toan >= 8.0 and Ngu_Van >= 6.5)) or (Toan >= 6.5 and Ngu_Van >= 8.0):
    if (
        Ly >= 6.5,
        Hoa >= 6.5,
        Tieng_Anh >= 6.5,
        Sinh_Hoc >= 6.5,
        Su >= 6.5,
        Dia >= 6.5,
        Tin_Hoc >= 6.5,
        GDCD >= 6.5,
        GDQPAN >= 6.5,
        GDTC >= 6.5,
    ):
        Tổng_Kết = (
            Toan
            + Ngu_Van
            + Ly
            + Hoa
            + Sinh_Hoc
            + Tin_Hoc
            + Tieng_Anh
            + Su
            + Dia
            + GDCD
            + GDTC
            + GDQPAN
        ) / 12
    if Tổng_Kết >= 8.0:
        print("Đạt danh hiệu học sinh Giỏi")
    else:
        print("Không đủ điều kiện là học sinh Giỏi")
if ((Toan >= 6.5 and Ngu_Van >= 5.0)) or (Toan >= 5.0 and Ngu_Van >= 6.5):
    if (
        Ly >= 5.0,
        Hoa >= 5.0,
        Tieng_Anh >= 5.0,
        Sinh_Hoc >= 5.0,
        Su >= 5.0,
        Dia >= 5.0,
        Tin_Hoc >= 5.0,
        GDCD >= 5.0,
        GDQPAN >= 5.0,
        GDTC >= 5.0,
    ):
        Tổng_Kết = (
            Toan
            + Ngu_Van
            + Ly
            + Hoa
            + Sinh_Hoc
            + Tin_Hoc
            + Tieng_Anh
            + Su
            + Dia
            + GDCD
            + GDTC
            + GDQPAN
        ) / 12
    if Tổng_Kết >= 6.5:
        print("Đạt danh hiệu học sinh Khá")
    else:
        print("Không đủ điều kiện là học sinh Khá")
