import pyotp
import time

# Mật khẩu cố định (trong thực tế, nên lưu trữ an toàn, ví dụ hash mật khẩu)
correct_password = "mypassword123"

# Xác thực bước 1: Kiểm tra mật khẩu
password = input("Nhập mật khẩu: ")
if password != correct_password:
    print("Mật khẩu không đúng! Xác thực thất bại.")
    exit()

print("Mật khẩu đúng! Tiến hành xác thực bước 2 (OTP)...")

# Xác thực bước 2: Tạo và kiểm tra mã OTP
secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key)

# Tạo mã OTP
otp = totp.now()
print(f"Mã OTP hiện tại: {otp}")

# Yêu cầu người dùng nhập mã OTP
user_input = input("Nhập mã OTP để xác thực: ")

# Kiểm tra mã OTP
if totp.verify(user_input):
    print("Xác thực 2FA thành công!")
else:
    print("Xác thực thất bại! Mã OTP không đúng.")

# Hiển thị thời gian còn lại trước khi mã OTP thay đổi
interval = 30
time_remaining = interval - (time.time() % interval)
print(f"Thời gian còn lại trước khi mã OTP thay đổi: {int(time_remaining)} giây")