'''Bài 1: Tính cước taxi ( 1đ )'''

distance = float(input("Nhập số km cần di chuyển: "))
car_type = int(input("Loại xe taxi (4 hoặc 7 chỗ): "))

if car_type == 4:
    # Tính cước taxi cho xe 4 chỗ
    if distance <= 0.8:
        cost = 11000
    elif distance <= 30:
        cost = 11000 + (distance - 0.8) * 15300
    else:
        cost = 11000 + 29.2 * 15300 + (distance - 30) * 12100
elif car_type == 7:
    # Tính cước taxi cho xe 7 chỗ
    if distance <= 0.8:
        cost = 12000
    elif distance <= 30:
        cost = 12000 + (distance - 0.8) * 16100
    else:
        cost = 12000 + 29.2 * 16100 + (distance - 30) * 13800
else:
    print("Loại xe không hợp lệ.")

# Tính cước tiền chờ
waiting_time = int(input("Nhập thời gian chờ (phút): "))
if waiting_time <= 5:
    waiting_cost = 0
else:
    waiting_cost = (waiting_time - 5) * 750

# Tổng cước taxi
total_cost = cost + waiting_cost
print("Tổng cước taxi là: ", total_cost, "đồng")


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
