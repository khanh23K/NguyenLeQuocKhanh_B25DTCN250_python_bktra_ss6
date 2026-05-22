# Viết chương trình tính tiền mua hàng cho khách.
# Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
# Tính Tổng tiền = Đơn giá * Số lượng.
# Áp dụng logic khuyến mãi:
# Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
# Nếu Tổng tiền < 1.000.000, không giảm giá.
# In ra màn hình số tiền cuối cùng khách phải thanh toán.
# câu 1
don_gia = int(input("Nhập vào giá đơn hàng của bạn: "))
so_luong = int(input("Nhập vào số lượng mà bạn muốn mua: "))
tong_tien = don_gia * so_luong
tien_duoc_giam = 0
if tong_tien >= 1000000:
    tien_duoc_giam = tong_tien * 0.9
    print(f"số tiền đc giảm 10% là: {tien_duoc_giam}")
elif tong_tien < 1000000:
    print("đơn của bạn quá ít chúng tôi ko thể giảm giá theo quy định!!!")
    print(f"số tiền đơn hàng của bạn là: {tong_tien}")

    