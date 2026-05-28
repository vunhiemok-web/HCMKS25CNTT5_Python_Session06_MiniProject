# Câu 1: Khởi động - Phân loại tình trạng hàng hóa
quantity = int(input("Nhập số lượng tồn kho của mì tôm: "))
if quantity >= 50:
    print("Tình trạng: Hàng đầy kho")
elif quantity >= 10:
    print("Tình trạng:  Mức an toàn")
else: 
    print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm")

# Câu 2: Vận dụng - Thống kê hàng lỗi thu hồi
sum_fail_product = 0
count = 0
while True:
    count += 1
    fail_product = int(input(f"số lượng hàng lỗi của quầy {count}: "))
    if fail_product == -1:
        print("Đã thống kê xong")
        break
    else:
        sum_fail_product += fail_product

print(f"Tổng số hàng lỗi thu hồi trong ngày là: {sum_fail_product}")

#Câu 3: Nâng cao - Xác thực lệnh xuất kho (3 điểm) 
ton_kho = 100
while True:
    out_quantity = int(input("Nhập số lượng muốn xuất: "))
    if out_quantity < 0:
        print("Không được nhập số âm, vui lòng nhập lại!")
    elif out_quantity > ton_kho:
        print("Kho không đủ hàng, vui lòng nhập lại!")
    else:
        ton_kho -= out_quantity
        print("Xuất kho thành công!")
        print(f"Tồn kho còn lại: {ton_kho}")
        break

        