# Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật (4 điểm) 
# Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình.
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