from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto. Cipher import AES
from Crypto. Random import get_random_bytes 
from Crypto. Util. Padding import pad, unpad 
import time
print("Khuất Thanh Phương")

# Tạo cặp khóa RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Mã hóa khóa AES bằng khóa công khai RSA
aes_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
start_time = time.time()
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

# Đo thời gian mã hóa AES
print("Thời gian mã hóa AES sau khi giải mã:", time.time() - start_time, "giây")

# Giải mã khóa AES bằng khóa bí mật RSA
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
start_time = time.time()
decrypted_aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Đo thời gian giải mã AES
print("Thời gian giải mã AES:", time.time() - start_time, "giây")