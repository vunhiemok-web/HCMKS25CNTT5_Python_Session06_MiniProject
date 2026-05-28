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