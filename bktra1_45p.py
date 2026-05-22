# # Viết chương trình tính tiền mua hàng cho khách.
# # Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
# # Tính Tổng tiền = Đơn giá * Số lượng.
# # Áp dụng logic khuyến mãi:
# # Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
# # Nếu Tổng tiền < 1.000.000, không giảm giá.
# # In ra màn hình số tiền cuối cùng khách phải thanh toán.
# # câu 1
# don_gia = int(input("Nhập vào giá đơn hàng của bạn: "))
# so_luong = int(input("Nhập vào số lượng mà bạn muốn mua: "))
# tong_tien = don_gia * so_luong
# tien_duoc_giam = 0
# if tong_tien >= 1000000:
#     tien_duoc_giam = tong_tien * 0.9
#     tong_tien_giam = tong_tien - tien_duoc_giam
#     print(f"số tiền đc giảm 10% là: {tien_duoc_giam}")
#     print(f"số tiền đơn hàng của bạn là: {tong_tien_giam}")
# elif tong_tien < 1000000:
#     print("đơn của bạn quá ít chúng tôi ko thể giảm giá theo quy định!!!")
#     print(f"số tiền đơn hàng của bạn là: {tong_tien}")
# # Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật (4 điểm) 
# # Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# # Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# # Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# # Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# # Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình.
trang_thai = True
mat_khau = 123456
for i in range(1,4):
    dang_nhap = int(input("vui lòng nhập mật khẩu của bạn: "))
    if dang_nhap != mat_khau:
        print("Mật khẩu sai, vui lòng nhập lại!")
        trang_thai = False
    elif dang_nhap == mat_khau:
        trang_thai = True
        break
if trang_thai == True:
    print("Đăng nhập thành công!") 
elif trang_thai == False:
    print("Tài khoản đã bị khóa!")
    