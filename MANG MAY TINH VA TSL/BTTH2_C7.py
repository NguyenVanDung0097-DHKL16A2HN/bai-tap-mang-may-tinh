from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto. Cipher import AES
from Crypto. Random import get_random_bytes 
from Crypto. Util. Padding import pad, unpad 
import time
print("Khuất Thanh Phương")
# Sinh cặp khóa RSA
rsa_key = RSA.generate(2048)
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

# Tạo khóa AES ngẫu nhiên và khởi tạo bộ mã hóa RSA
aes_key = get_random_bytes(16)
encryptor_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))

# Mã hóa khóa AES bằng RSA
start_encrypt = time.time()
encrypted_aes_key = encryptor_rsa.encrypt(aes_key)
end_encrypt = time.time()
encryption_duration = end_encrypt - start_encrypt

print("Khóa AES đã được mã hóa bằng RSA:", encrypted_aes_key)
print("Thời gian mã hóa RSA:", encryption_duration, "giây")

# Giải mã khóa AES bằng khóa bí mật RSA
decryptor_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
start_decrypt = time.time()
decrypted_aes_key = decryptor_rsa.decrypt(encrypted_aes_key)
end_decrypt = time.time()
decryption_duration = end_decrypt - start_decrypt

print("Khóa AES sau khi giải mã:", decrypted_aes_key)
print("Thời gian giải mã RSA:", decryption_duration, "giây")