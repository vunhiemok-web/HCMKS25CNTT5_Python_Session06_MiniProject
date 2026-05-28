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