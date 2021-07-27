import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
chars = digits + lowercase_letters + uppercase_letters + punctuation

cntPw = input('Укажите количество паролей для генерации:')
lenPw = input('Укажите длину одного пароля:')

def generate_password(length, chars):
    p = ''
    for i in range(0, int(lenPw), 4):
        p += random.choice(chars[0:9])
        p += random.choice(chars[10:36])
        p += random.choice(chars[37:63])
        p += random.choice(chars[64:77])
    random.shuffle(list(p))
    return p[0: int(lenPw)]

for m in range(int(cntPw)):
    print(generate_password(lenPw, chars))