import socket

# Tạo socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối tới server tại IP và cổng 5000
client_socket.connect(("127.0.0.1", 5000))

# Gửi dữ liệu tới server
client_socket.send("Hello Server!".encode())

# Nhận phản hồi từ server
message = client_socket.recv(5000).decode()
print("📩 Tin nhắn từ server:", message)

# Gửi lệnh "exit" để đóng server
client_socket.send("exit".encode())

# Đóng kết nối
client_socket.close()
