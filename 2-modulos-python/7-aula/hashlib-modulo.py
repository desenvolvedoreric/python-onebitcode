import hashlib

message = "Eric, socorro!".encode()

encoded = hashlib.sha256()
encoded.update(message)
print(encoded.hexdigest())