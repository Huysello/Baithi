'''Bài 2: Đếm số ký tự hoa và số ký tự thường trong chuỗi (3 đ)'''

def dem_ky_tu_hoa_thuong(chuoi):
    hoa = 0
    thuong = 0
    for ky_tu in chuoi:
        if ky_tu.isupper():
            hoa += 1
        elif ky_tu.islower():
            thuong += 1
    return hoa, thuong

chuoi = input("Nhập chuỗi: ")
so_luong_hoa, so_luong_thuong = dem_ky_tu_hoa_thuong(chuoi)
print("Số lượng ký tự hoa trong chuỗi là:", so_luong_hoa)
print("Số lượng ký tự thường trong chuỗi là:", so_luong_thuong)
