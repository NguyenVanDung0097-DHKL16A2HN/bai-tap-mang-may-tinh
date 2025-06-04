import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind("127.0.0.1"), 80
server_socket.listen(5)
print("Server đang lắng nghe kết nối trên cổng 80_")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ {client_address}")
    
    data = client_socket.recv(1024).decode()
    print(f"Dữ liệu nhận được: {data}")
    
    response = "Server đã nhận dữ liệu từ client!"
    client_socket.send(response.encode())
    client_socket.close()
    
    if data.lower() == "exit":
        print("Server đang tắt ...")
        break
server_socket.close()