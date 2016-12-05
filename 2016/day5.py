from hashlib import md5

door = 'reyedfim'
password = ''
more_secure_password = list('________')
index = 0

while len(password) < 8 or '_' in more_secure_password:
    hashed = md5((door + str(index)).encode()).hexdigest()
    if hashed[0:5] == '00000':
        value = hashed[5]
        if len(password) < 8:
            password += value
        if value in list(map(str, range(0, 8))) and more_secure_password[int(value)] == '_':
            more_secure_password[int(value)] = hashed[6]
    index += 1

print(password)
print(''.join(more_secure_password))
